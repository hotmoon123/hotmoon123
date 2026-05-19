from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, Q, Avg, F
from django.utils import timezone
from decimal import Decimal

from apps.properties.models import Property
from apps.leases.models import Lease
from apps.financials.models import Invoice, Transaction
from apps.financials.services import (
    build_landlord_activity_feed,
    format_currency_compact,
    landlord_maintenance_donut_counts,
    landlord_monthly_revenue_series,
    landlord_weekly_revenue_series,
    occupied_distinct_properties_from_leases,
    transaction_sum_in_month,
)
from apps.maintenance.models import MaintenanceTicket
from apps.users.models import Landlord, Tenant
from apps.users.permissions import IsLandlord


def index_view(request):
    """Public marketing landing page."""
    return render(request, "public/landing.html")


def login_page(request):
    """Login page for all users."""
    return render(request, "public/login.html")


def register_page(request):
    """Registration page for all users."""
    return render(request, "public/register.html")


def forgot_password_page(request):
    """Forgot password page."""
    return render(request, "public/forgot_password.html")


def reset_password_page(request):
    """Reset password page."""
    return render(request, "public/reset_password.html")


def verify_email_page(request):
    """Email verification page."""
    return render(request, "public/verify_email.html")


# ─── Landlord Pages ────────────────────────────────────────────


def landlord_dashboard(request):
    """Landlord dashboard — command center (spec §1 Page 1 + analytics chart patterns)."""
    # Ensure user is authenticated and is a landlord
    if not request.user.is_authenticated:
        return redirect('login_page')
    
    if isinstance(request.user, Tenant):
        return redirect('tenant_dashboard')
    if not isinstance(request.user, Landlord):
        return redirect('login_page')
    
    user = request.user
    today_d = timezone.localdate()
    now = timezone.now()
    
    # Fetch real metrics from database
    properties = Property.objects.filter(landlord=user)
    total_properties = properties.count()
    occupied_properties = properties.filter(status='occupied').count()
    occupancy_rate = (occupied_properties / total_properties * 100) if total_properties > 0 else 0
    
    # Monthly revenue from paid invoices (actual collected this calendar month)
    current_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    monthly_revenue = Invoice.objects.filter(
        landlord=user,
        status='paid',
        paid_at__gte=current_month
    ).aggregate(total=Sum('amount_paid'))['total'] or Decimal('0.00')
    
    # Open maintenance tickets
    open_tickets = MaintenanceTicket.objects.filter(
        landlord=user,
        status__in=['todo', 'in_progress', 'pending_parts']
    ).count()
    
    overdue_q = Q(status='overdue') | Q(
        status__in=['unpaid', 'partial'],
        due_date__lt=today_d,
    )
    overdue_count = Invoice.objects.filter(landlord=user).filter(overdue_q).count()

    # MoM payment volume (transactions) for trend chip
    cy, cm = today_d.year, today_d.month
    if cm == 1:
        py, pm = cy - 1, 12
    else:
        py, pm = cy, cm - 1
    this_tx = transaction_sum_in_month(user, cy, cm)
    last_tx = transaction_sum_in_month(user, py, pm)
    if last_tx > 0:
        revenue_mom_pct = float((this_tx - last_tx) / last_tx * 100)
    elif this_tx > 0:
        revenue_mom_pct = 100.0
    else:
        revenue_mom_pct = 0.0
    if revenue_mom_pct > 0.5:
        revenue_trend_label = f"↑ +{revenue_mom_pct:.0f}%"
    elif revenue_mom_pct < -0.5:
        revenue_trend_label = f"↓ {revenue_mom_pct:.0f}%"
    else:
        revenue_trend_label = "→ same"

    last_day_prev_month = today_d.replace(day=1) - timezone.timedelta(days=1)
    occ_now = occupied_distinct_properties_from_leases(user, today_d)
    occ_prev = occupied_distinct_properties_from_leases(user, last_day_prev_month)
    occ_delta_units = occ_now - occ_prev
    if occ_delta_units > 0:
        occupancy_trend_label = f"↑ +{occ_delta_units}"
    elif occ_delta_units < 0:
        occupancy_trend_label = f"↓ {occ_delta_units}"
    else:
        occupancy_trend_label = "→ same"

    created_7d = MaintenanceTicket.objects.filter(
        landlord=user, created_at__gte=now - timezone.timedelta(days=7)
    ).count()
    resolved_7d = MaintenanceTicket.objects.filter(
        landlord=user,
        status='done',
        updated_at__gte=now - timezone.timedelta(days=7),
    ).count()
    net_tickets = created_7d - resolved_7d
    if net_tickets > 0:
        ticket_trend_label = f"↑ +{net_tickets}"
    elif net_tickets < 0:
        ticket_trend_label = f"↓ {net_tickets}"
    else:
        ticket_trend_label = "→ same"

    overdue_trend_label = "All clear" if overdue_count == 0 else f"{overdue_count} open"

    # Expiring leases (next 60 days)
    sixty_days_from_now = today_d + timezone.timedelta(days=60)
    expiring_leases = list(
        Lease.objects.filter(
            landlord=user,
            status='active',
            end_date__lte=sixty_days_from_now,
            end_date__gte=today_d,
        ).select_related('tenant', 'property')[:8]
    )
    expiring_rows = []
    for lease in expiring_leases:
        days_left = (lease.end_date - today_d).days
        if days_left < 14:
            urgency = "critical"
        elif days_left < 30:
            urgency = "warn"
        else:
            urgency = "ok"
        tenant_label = ""
        if lease.tenant_id:
            t = lease.tenant
            tenant_label = (f"{t.first_name} {t.last_name}".strip() or t.email)
        expiring_rows.append(
            {
                "lease": lease,
                "days_left": days_left,
                "urgency": urgency,
                "tenant_label": tenant_label,
            }
        )
    
    # Recent transactions (detail list below fold)
    recent_transactions = Transaction.objects.filter(
        landlord=user
    ).select_related('invoice', 'tenant').order_by('-created_at')[:10]

    revenue_chart = landlord_monthly_revenue_series(user, num_months=12)
    revenue_weekly = landlord_weekly_revenue_series(user, num_weeks=12)
    maintenance_donut = landlord_maintenance_donut_counts(user)
    activity_feed = build_landlord_activity_feed(user, limit=25)

    hour = now.hour
    if hour < 12:
        greeting = "Good morning"
    elif hour < 17:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    first_name = (user.first_name or "").strip() or "there"

    # JSON-serializable snapshot for dashboard CSV export (client-side download)
    dashboard_export = {
        "generated_at": now.isoformat(),
        "summary": {
            "total_properties": total_properties,
            "occupied_properties": occupied_properties,
            "occupancy_rate_percent": float(round(occupancy_rate, 1)),
            "monthly_revenue": str(monthly_revenue),
            "open_maintenance_tickets": open_tickets,
            "overdue_invoices": overdue_count,
        },
        "revenue_by_month": [
            {"month_label": lab, "amount": val}
            for lab, val in zip(revenue_chart["labels"], revenue_chart["values"])
        ],
        "revenue_by_week": [
            {"week_label": lab, "amount": val}
            for lab, val in zip(revenue_weekly["labels"], revenue_weekly["values"])
        ],
        "maintenance_donut": maintenance_donut,
        "expiring_leases": [
            {
                "unit": row["lease"].property.unit_number if row["lease"].property else "",
                "end_date": row["lease"].end_date.isoformat(),
                "tenant_email": row["lease"].tenant.email if row["lease"].tenant else "",
                "days_left": row["days_left"],
            }
            for row in expiring_rows
        ],
        "recent_transactions": [
            {
                "created_at": tx.created_at.isoformat(),
                "amount": str(tx.amount),
                "tenant_email": tx.tenant.email,
                "reference": tx.gateway_reference or "",
            }
            for tx in recent_transactions
        ],
    }

    context = {
        'total_properties': total_properties,
        'occupied_properties': occupied_properties,
        'occupancy_rate': round(occupancy_rate, 1),
        'monthly_revenue': monthly_revenue,
        'monthly_revenue_compact': format_currency_compact(monthly_revenue, "KES"),
        'open_tickets': open_tickets,
        'overdue_count': overdue_count,
        'expiring_leases': expiring_leases,
        'expiring_rows': expiring_rows,
        'recent_transactions': recent_transactions,
        'dashboard_export': dashboard_export,
        'revenue_chart': revenue_chart,
        'maintenance_donut': maintenance_donut,
        'activity_feed': activity_feed,
        'greeting': greeting,
        'first_name': first_name,
        'revenue_trend_label': revenue_trend_label,
        'occupancy_trend_label': occupancy_trend_label,
        'overdue_trend_label': overdue_trend_label,
        'ticket_trend_label': ticket_trend_label,
        'currency_code': 'KES',
        'page_updated_at': now,
    }
    
    return render(request, "landlord/dashboard.html", context)


def landlord_properties(request):
    """Property portfolio management."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if isinstance(request.user, Tenant):
        return redirect('tenant_dashboard')
    if not isinstance(request.user, Landlord):
        return redirect('login_page')
    return render(
        request,
        "landlord/properties.html",
        {"property_type_choices": Property.TYPE_CHOICES},
    )


def landlord_leases(request):
    """Lease management page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if isinstance(request.user, Tenant):
        return redirect('tenant_dashboard')
    if not isinstance(request.user, Landlord):
        return redirect('login_page')
    return render(request, "landlord/leases.html")


def landlord_financials(request):
    """Financial management page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if isinstance(request.user, Tenant):
        return redirect('tenant_dashboard')
    if not isinstance(request.user, Landlord):
        return redirect('login_page')
    return render(request, "landlord/financials.html")


def landlord_tenants(request):
    """Tenant directory page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if isinstance(request.user, Tenant):
        return redirect('tenant_dashboard')
    if not isinstance(request.user, Landlord):
        return redirect('login_page')

    tenant_ids = (
        Lease.objects.filter(
            landlord=request.user,
            tenant__isnull=False,
            deleted_at__isnull=True,
        )
        .values_list("tenant_id", flat=True)
        .distinct()
    )
    tenants_qs = Tenant.objects.filter(pk__in=tenant_ids).order_by(
        "last_name", "first_name", "email"
    )

    tenant_rows = []
    for t in tenants_qs:
        lease = (
            Lease.objects.filter(
                landlord=request.user,
                tenant=t,
                deleted_at__isnull=True,
            )
            .select_related("property", "property__building")
            .order_by("-start_date")
            .first()
        )
        tenant_rows.append({"tenant": t, "lease": lease})

    return render(
        request,
        "landlord/tenants.html",
        {"tenant_rows": tenant_rows},
    )


def landlord_maintenance(request):
    """Maintenance kanban board."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if isinstance(request.user, Tenant):
        return redirect('tenant_dashboard')
    if not isinstance(request.user, Landlord):
        return redirect('login_page')
    return render(request, "landlord/maintenance.html")


def landlord_chat(request):
    """Real-time chat page — tenant list from leases; thread UI (WS sync later)."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if isinstance(request.user, Tenant):
        return redirect('tenant_dashboard')
    if not isinstance(request.user, Landlord):
        return redirect('login_page')

    tenant_ids = (
        Lease.objects.filter(
            landlord=request.user,
            tenant__isnull=False,
            deleted_at__isnull=True,
        )
        .values_list("tenant_id", flat=True)
        .distinct()
    )
    chat_contacts = []
    for tid in tenant_ids:
        try:
            t = Tenant.objects.get(pk=tid)
        except Tenant.DoesNotExist:
            continue
        lease = (
            Lease.objects.filter(
                landlord=request.user,
                tenant=t,
                deleted_at__isnull=True,
            )
            .select_related("property")
            .order_by("-start_date")
            .first()
        )
        unit = (
            lease.property.unit_number
            if lease and lease.property
            else "—"
        )
        initials = ""
        if t.first_name and t.last_name:
            initials = (t.first_name[0] + t.last_name[0]).upper()
        elif t.first_name:
            initials = t.first_name[:2].upper()
        else:
            initials = (t.email[:2] or "?").upper()
        chat_contacts.append(
            {
                "id": t.pk,
                "name": t.full_name,
                "email": t.email,
                "unit": unit,
                "initials": initials,
            }
        )
    chat_contacts.sort(key=lambda c: c["name"].lower())

    return render(
        request,
        "landlord/chat.html",
        {"chat_contacts": chat_contacts},
    )


def landlord_documents(request):
    """Document management page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if isinstance(request.user, Tenant):
        return redirect('tenant_dashboard')
    if not isinstance(request.user, Landlord):
        return redirect('login_page')
    return render(request, "landlord/documents.html")


def landlord_analytics(request):
    """Analytics and reporting page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if isinstance(request.user, Tenant):
        return redirect('tenant_dashboard')
    if not isinstance(request.user, Landlord):
        return redirect('login_page')
    return render(request, "landlord/analytics.html")


def landlord_notifications(request):
    """Notification center page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if isinstance(request.user, Tenant):
        return redirect('tenant_dashboard')
    if not isinstance(request.user, Landlord):
        return redirect('login_page')
    return render(request, "landlord/notifications.html")


def landlord_settings(request):
    """Settings and profile page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if isinstance(request.user, Tenant):
        return redirect('tenant_dashboard')
    if not isinstance(request.user, Landlord):
        return redirect('login_page')
    return render(request, "landlord/settings.html")


def landlord_automations(request):
    """Automation control panel page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if isinstance(request.user, Tenant):
        return redirect('tenant_dashboard')
    if not isinstance(request.user, Landlord):
        return redirect('login_page')
    return render(request, "landlord/automations.html")


def landlord_buildings(request):
    """Multi-unit building management page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if isinstance(request.user, Tenant):
        return redirect('tenant_dashboard')
    if not isinstance(request.user, Landlord):
        return redirect('login_page')
    return render(request, "landlord/buildings.html")


def landlord_expenses(request):
    """Expense and ROI ledger page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if isinstance(request.user, Tenant):
        return redirect('tenant_dashboard')
    if not isinstance(request.user, Landlord):
        return redirect('login_page')
    return render(request, "landlord/expenses.html")


# ─── Tenant Pages ─────────────────────────────────────────────


def tenant_dashboard(request):
    """Tenant dashboard with balance overview."""
    # Ensure user is authenticated and is a tenant
    if not request.user.is_authenticated:
        return redirect('login_page')
    
    if isinstance(request.user, Landlord):
        return redirect('landlord_dashboard')
    if not isinstance(request.user, Tenant):
        return redirect('login_page')
    
    user = request.user
    
    # Get tenant's active lease
    active_lease = Lease.objects.filter(
        tenant=user,
        status='active'
    ).select_related('property', 'landlord').first()
    
    # Get outstanding invoices
    outstanding_invoices = Invoice.objects.filter(
        tenant=user,
        status__in=['unpaid', 'partial', 'overdue']
    ).order_by('due_date')
    
    # Total balance due (amount still owed on open invoices)
    total_balance = outstanding_invoices.aggregate(
        total=Sum(F('amount') - F('amount_paid'))
    )['total'] or Decimal('0.00')
    
    # Next payment (earliest due date)
    next_payment = outstanding_invoices.first()
    
    # Recent notices/notifications (you can add a Notification model later)
    # For now, using recent invoices as activity
    recent_activity = Invoice.objects.filter(
        tenant=user
    ).order_by('-created_at')[:5]
    
    context = {
        'active_lease': active_lease,
        'outstanding_invoices': outstanding_invoices,
        'total_balance': total_balance,
        'next_payment': next_payment,
        'recent_activity': recent_activity,
    }
    
    return render(request, "tenant/dashboard.html", context)


def tenant_payments(request):
    """Rent payment page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if isinstance(request.user, Landlord):
        return redirect('landlord_dashboard')
    if not isinstance(request.user, Tenant):
        return redirect('login_page')
    return render(request, "tenant/payments.html")


def tenant_lease(request):
    """Lease details page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if isinstance(request.user, Landlord):
        return redirect('landlord_dashboard')
    if not isinstance(request.user, Tenant):
        return redirect('login_page')
    return render(request, "tenant/lease.html")


def tenant_maintenance(request):
    """Maintenance ticket submission page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if isinstance(request.user, Landlord):
        return redirect('landlord_dashboard')
    if not isinstance(request.user, Tenant):
        return redirect('login_page')
    return render(request, "tenant/maintenance.html")


def tenant_chat(request):
    """Chat with landlord page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if isinstance(request.user, Landlord):
        return redirect('landlord_dashboard')
    if not isinstance(request.user, Tenant):
        return redirect('login_page')
    return render(request, "tenant/chat.html")


def tenant_inspection(request):
    """Move-in/move-out inspection page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if isinstance(request.user, Landlord):
        return redirect('landlord_dashboard')
    if not isinstance(request.user, Tenant):
        return redirect('login_page')
    return render(request, "tenant/inspection.html")


def tenant_payment_methods(request):
    """Payment methods management page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if isinstance(request.user, Landlord):
        return redirect('landlord_dashboard')
    if not isinstance(request.user, Tenant):
        return redirect('login_page')
    return render(request, "tenant/payment_methods.html")


def tenant_notice_board(request):
    """Landlord notice board page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if isinstance(request.user, Landlord):
        return redirect('landlord_dashboard')
    if not isinstance(request.user, Tenant):
        return redirect('login_page')
    return render(request, "tenant/notice_board.html")


def tenant_compliance(request):
    """Compliance documents page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if isinstance(request.user, Landlord):
        return redirect('landlord_dashboard')
    if not isinstance(request.user, Tenant):
        return redirect('login_page')
    return render(request, "tenant/compliance.html")


def tenant_profile(request):
    """Profile settings page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if isinstance(request.user, Landlord):
        return redirect('landlord_dashboard')
    if not isinstance(request.user, Tenant):
        return redirect('login_page')
    return render(request, "tenant/profile.html")


def tenant_history(request):
    """Payment history page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if isinstance(request.user, Landlord):
        return redirect('landlord_dashboard')
    if not isinstance(request.user, Tenant):
        return redirect('login_page')
    return render(request, "tenant/history.html")


# ─── Public Pages ─────────────────────────────────────────────


def payment_success(request):
    """Payment success page."""
    return render(request, "public/payment_success.html")


def payment_cancelled(request):
    """Payment cancelled page."""
    return render(request, "public/payment_cancelled.html")


def error_403(request, exception):
    """403 Forbidden page."""
    return render(
        request,
        "public/error_generic.html",
        {
            "error_code": "403",
            "error_title": "Forbidden",
            "error_message": "You do not have permission to access this resource.",
        },
        status=403,
    )


def error_404(request, exception):
    """404 Not Found page."""
    return render(
        request,
        "public/error_generic.html",
        {
            "error_code": "404",
            "error_title": "Page Not Found",
            "error_message": "The page you requested does not exist.",
        },
        status=404,
    )


def error_429(request, exception=None):
    """429 Too Many Requests page."""
    return render(
        request,
        "public/error_generic.html",
        {
            "error_code": "429",
            "error_title": "Too Many Requests",
            "error_message": "Please wait before trying again.",
        },
        status=429,
    )


def error_500(request):
    """500 Server Error page."""
    return render(
        request,
        "public/error_generic.html",
        {
            "error_code": "500",
            "error_title": "Server Error",
            "error_message": "Something went wrong on our side. Please try again shortly.",
        },
        status=500,
    )
