"""Domain helpers for invoices, payments, and landlord reporting."""

from __future__ import annotations

from datetime import date, datetime, time, timedelta
from decimal import Decimal

from django.db.models import Q, Sum
from django.db.models.functions import TruncWeek
from django.utils import formats, timezone

from apps.financials.models import Invoice, Transaction


def _ts_display(dt) -> str:
    if dt is None:
        return ""
    return formats.date_format(timezone.localtime(dt), "M j, g:i a")


def _month_index_to_ym(month_index: int) -> tuple[int, int]:
    return month_index // 12, month_index % 12 + 1


def _month_range_aware(year: int, month: int, tz) -> tuple[datetime, datetime]:
    start_d = date(year, month, 1)
    if month == 12:
        end_d = date(year + 1, 1, 1)
    else:
        end_d = date(year, month + 1, 1)
    lo = timezone.make_aware(datetime.combine(start_d, time.min), tz)
    hi = timezone.make_aware(datetime.combine(end_d, time.min), tz)
    return lo, hi


def transaction_sum_in_month(landlord, year: int, month: int) -> Decimal:
    tz = timezone.get_current_timezone()
    lo, hi = _month_range_aware(year, month, tz)
    return (
        Transaction.objects.filter(landlord=landlord, created_at__gte=lo, created_at__lt=hi).aggregate(
            t=Sum("amount")
        )["t"]
        or Decimal("0")
    )


def landlord_monthly_revenue_series(landlord, num_months: int = 12) -> dict:
    """
    Sum ``Transaction.amount`` per calendar month for the trailing ``num_months``
    months (ending with the current month). Labels like ``Jan '26``.
    """
    num_months = max(1, min(int(num_months), 36))
    today = timezone.localdate()
    cur_mi = today.year * 12 + today.month - 1
    start_mi = cur_mi - (num_months - 1)
    labels = []
    values = []
    for mi in range(start_mi, cur_mi + 1):
        y, m = _month_index_to_ym(mi)
        total = transaction_sum_in_month(landlord, y, m)
        labels.append(date(y, m, 1).strftime("%b '%y"))
        values.append(float(total))
    return {"labels": labels, "values": values}


def landlord_weekly_revenue_series(landlord, num_weeks: int = 12) -> dict:
    """
    Sum Transaction.amount per calendar week (ISO Monday start) for the last
    `num_weeks` weeks, including partial current week.

    Returns JSON-friendly ``{"labels": [...], "values": [...]}`` for charts.
    """
    num_weeks = max(1, min(int(num_weeks), 52))
    today = timezone.localdate()
    this_monday = today - timedelta(days=today.weekday())
    oldest_monday = this_monday - timedelta(weeks=num_weeks - 1)
    tz = timezone.get_current_timezone()
    start_dt = timezone.make_aware(datetime.combine(oldest_monday, time.min), tz)

    rows = (
        Transaction.objects.filter(landlord=landlord, created_at__gte=start_dt)
        .annotate(week=TruncWeek("created_at", tzinfo=tz))
        .values("week")
        .annotate(total=Sum("amount"))
        .order_by("week")
    )

    totals: dict = {}
    for row in rows:
        w = row["week"]
        if not w:
            continue
        d = timezone.localtime(w, tz).date()
        mon = d - timedelta(days=d.weekday())
        amt = row["total"] or Decimal("0")
        totals[mon] = totals.get(mon, Decimal("0")) + amt

    labels = []
    values = []
    for i in range(num_weeks):
        d = oldest_monday + timedelta(weeks=i)
        labels.append(d.strftime("%b %d"))
        values.append(float(totals.get(d, Decimal("0"))))

    return {"labels": labels, "values": values}


def format_currency_compact(amount: Decimal | float, code: str = "KES") -> str:
    """Human-readable compact money (e.g. ``KES 84K``)."""
    f = float(amount) if not isinstance(amount, Decimal) else float(amount)
    if f >= 1_000_000:
        return f"{code} {f / 1_000_000:.1f}M"
    if f >= 1000:
        return f"{code} {f / 1000:.0f}K"
    if f >= 1:
        return f"{code} {f:.0f}"
    return f"{code} 0"


def landlord_maintenance_donut_counts(landlord) -> dict:
    """Bucket ticket statuses for dashboard donut (Resolved / In progress / Pending)."""
    from django.db.models import Count

    from apps.maintenance.models import MaintenanceTicket

    rows = MaintenanceTicket.objects.filter(landlord=landlord).values("status").annotate(c=Count("id"))
    by_status = {r["status"]: r["c"] for r in rows}
    resolved = int(by_status.get("done", 0))
    in_progress = int(by_status.get("in_progress", 0))
    pending = int(by_status.get("todo", 0)) + int(by_status.get("pending_parts", 0))
    return {"resolved": resolved, "in_progress": in_progress, "pending": pending}


def occupied_distinct_properties_from_leases(landlord, on_date: date) -> int:
    """Count distinct properties with an active lease covering ``on_date``."""
    from apps.leases.models import Lease

    return (
        Lease.objects.filter(
            landlord=landlord,
            status="active",
            start_date__lte=on_date,
            end_date__gte=on_date,
        )
        .values("property_id")
        .distinct()
        .count()
    )


def build_landlord_activity_feed(landlord, limit: int = 25) -> list[dict]:
    """
    Merge recent payments, invoices, tickets, and leases into one timeline
    for the dashboard activity panel (JSON-serializable).
    """
    from apps.leases.models import Lease
    from apps.maintenance.models import MaintenanceTicket

    items: list[dict] = []
    today = timezone.localdate()

    for tx in (
        Transaction.objects.filter(landlord=landlord)
        .select_related("tenant", "invoice__lease__property")
        .order_by("-created_at")[:40]
    ):
        unit = ""
        if tx.invoice_id and getattr(tx.invoice, "lease", None):
            prop = getattr(tx.invoice.lease, "property", None)
            if prop:
                unit = prop.unit_number or ""
        meta_parts = [tx.tenant.email if tx.tenant else "Tenant"]
        if unit:
            meta_parts.append(f"Unit {unit}")
        meta_parts.append(f"{format_currency_compact(tx.amount)}")
        items.append(
            {
                "id": f"tx-{tx.id}",
                "kind": "payment",
                "icon": "emerald",
                "title": "Rent received",
                "meta": " · ".join(meta_parts),
                "ts": tx.created_at.isoformat(),
                "ts_display": _ts_display(tx.created_at),
            }
        )

    inv_q = (
        Invoice.objects.filter(landlord=landlord)
        .filter(Q(status="overdue") | Q(status__in=["unpaid", "partial"], due_date__lt=today))
        .select_related("tenant", "lease__property")
        .order_by("-updated_at")[:20]
    )
    for inv in inv_q:
        unit = ""
        if inv.lease_id and inv.lease.property_id:
            unit = inv.lease.property.unit_number or ""
        tenant_email = inv.tenant.email if inv.tenant else ""
        label = "Overdue rent" if inv.status == "overdue" or inv.due_date < today else "Balance due"
        meta = tenant_email + (f" · Unit {unit}" if unit else "")
        items.append(
            {
                "id": f"inv-{inv.id}",
                "kind": "overdue",
                "icon": "red",
                "title": label,
                "meta": meta or "Invoice",
                "ts": inv.updated_at.isoformat(),
                "ts_display": _ts_display(inv.updated_at),
            }
        )

    for ticket in (
        MaintenanceTicket.objects.filter(landlord=landlord)
        .select_related("property")
        .order_by("-created_at")[:25]
    ):
        unit = ticket.property.unit_number if ticket.property_id else ""
        items.append(
            {
                "id": f"tk-{ticket.id}",
                "kind": "ticket",
                "icon": "blue",
                "title": ticket.title[:80],
                "meta": f"Unit {unit}" if unit else "Maintenance",
                "ts": ticket.created_at.isoformat(),
                "ts_display": _ts_display(ticket.created_at),
            }
        )

    for lease in (
        Lease.objects.filter(landlord=landlord, status="active")
        .select_related("tenant", "property")
        .order_by("-created_at")[:15]
    ):
        if not lease.tenant_id:
            continue
        unit = lease.property.unit_number if lease.property_id else ""
        items.append(
            {
                "id": f"lease-{lease.id}",
                "kind": "tenant",
                "icon": "amber",
                "title": "Active lease",
                "meta": f"{lease.tenant.email} · Unit {unit}" if unit else lease.tenant.email,
                "ts": lease.created_at.isoformat(),
                "ts_display": _ts_display(lease.created_at),
            }
        )

    items.sort(key=lambda x: x["ts"], reverse=True)
    return items[:limit]
