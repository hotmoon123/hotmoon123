"""
Financials App — Django MVT Views
Returns JSON for AJAX calls from the frontend JS.
"""
import json
import uuid
from decimal import Decimal
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.db.models import Sum, Q, F
from django.utils import timezone

from apps.users.models import Landlord
from .models import Invoice, Transaction, Expense, PaymentMethod


def invoice_to_dict(inv):
    return {
        'id': inv.pk,
        'amount': str(inv.amount),
        'amount_paid': str(inv.amount_paid),
        'status': inv.status,
        'due_date': inv.due_date.isoformat() if inv.due_date else None,
        'paid_at': inv.paid_at.isoformat() if inv.paid_at else None,
        'tenant_id': inv.tenant_id,
        'landlord_id': inv.landlord_id,
    }


@login_required
@require_http_methods(['GET'])
def invoice_list(request):
    user = request.user
    if isinstance(user, Landlord):
        qs = Invoice.objects.filter(landlord=user).select_related('tenant', 'lease')
    else:
        qs = Invoice.objects.filter(tenant=user).select_related('landlord', 'lease')
    return JsonResponse({'results': [invoice_to_dict(i) for i in qs]})


@login_required
@require_http_methods(['POST'])
def invoice_create(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'errors': {'detail': 'Invalid JSON.'}}, status=400)

    from apps.leases.models import Lease
    errors = {}
    lease_id = data.get('lease_id')
    amount = data.get('amount')
    due_date = data.get('due_date')

    if not lease_id: errors['lease_id'] = 'Lease is required.'
    if not amount: errors['amount'] = 'Amount is required.'
    if not due_date: errors['due_date'] = 'Due date is required.'

    if errors:
        return JsonResponse({'success': False, 'errors': errors}, status=400)

    try:
        lease = Lease.objects.get(pk=lease_id, landlord=request.user)
    except Lease.DoesNotExist:
        return JsonResponse({'success': False, 'errors': {'lease_id': 'Lease not found.'}}, status=404)

    invoice = Invoice.objects.create(
        landlord=lease.landlord,
        tenant=lease.tenant,
        lease=lease,
        amount=Decimal(str(amount)),
        amount_paid=Decimal('0.00'),
        due_date=due_date,
        status='unpaid',
    )
    return JsonResponse({'success': True, 'invoice': invoice_to_dict(invoice)}, status=201)


@login_required
@require_http_methods(['GET'])
def invoice_outstanding(request):
    today = timezone.now().date()
    qs = Invoice.objects.filter(
        tenant=request.user,
        status__in=['unpaid', 'partial', 'overdue'],
        due_date__lt=today,
    ).order_by('due_date')
    return JsonResponse({'results': [invoice_to_dict(i) for i in qs]})


@login_required
@require_http_methods(['GET'])
def invoice_summary(request):
    user = request.user
    if isinstance(user, Landlord):
        qs = Invoice.objects.filter(landlord=user)
    else:
        qs = Invoice.objects.filter(tenant=user)

    total_outstanding = qs.filter(status__in=['unpaid', 'partial', 'overdue']).aggregate(
        total=Sum('amount')
    )['total'] or Decimal('0.00')

    overdue_count = qs.filter(
        status__in=['unpaid', 'partial'],
        due_date__lt=timezone.now().date()
    ).count()

    current_month = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    paid_this_month = qs.filter(
        status='paid', paid_at__gte=current_month
    ).aggregate(total=Sum('amount_paid'))['total'] or Decimal('0.00')

    return JsonResponse({
        'total_outstanding': float(total_outstanding),
        'overdue_count': overdue_count,
        'paid_this_month': float(paid_this_month),
    })


@login_required
@require_http_methods(['POST'])
def payment_pay(request):
    """Tenant submits payment for an invoice."""
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'errors': {'detail': 'Invalid JSON.'}}, status=400)

    invoice_id = data.get('invoice_id')
    if not invoice_id:
        return JsonResponse({'success': False, 'errors': {'invoice_id': 'Invoice ID is required.'}}, status=400)

    try:
        invoice = Invoice.objects.get(pk=invoice_id, tenant=request.user)
    except Invoice.DoesNotExist:
        return JsonResponse({'success': False, 'errors': {'detail': 'Invoice not found.'}}, status=404)

    if invoice.status == 'paid':
        return JsonResponse({'success': False, 'errors': {'detail': 'Invoice already paid.'}}, status=400)

    tenant = request.user
    idempotency_key = f"{tenant.id}_{invoice.id}_{timezone.now().date()}"

    if Transaction.objects.filter(idempotency_key=idempotency_key).exists():
        return JsonResponse(
            {'success': False, 'errors': {'detail': 'This payment has already been processed.'}},
            status=400
        )

    gateway_reference = f"txn_{uuid.uuid4().hex[:16]}"

    transaction = Transaction.objects.create(
        invoice=invoice,
        tenant=tenant,
        landlord=invoice.landlord,
        amount=invoice.amount,
        gateway_reference=gateway_reference,
        idempotency_key=idempotency_key,
    )

    invoice.status = 'paid'
    invoice.amount_paid = invoice.amount
    invoice.paid_at = timezone.now()
    invoice.save()

    return JsonResponse({
        'success': True,
        'message': 'Payment successful.',
        'receipt_id': gateway_reference,
    })


@login_required
@require_http_methods(['GET'])
def expense_list(request):
    qs = Expense.objects.filter(landlord=request.user).select_related('rental_property')
    return JsonResponse({'results': [
        {
            'id': e.pk,
            'category': e.category,
            'amount': str(e.amount),
            'description': e.description,
            'expense_date': e.expense_date.isoformat() if e.expense_date else None,
            'property_id': e.rental_property_id,
        }
        for e in qs
    ]})


@login_required
@require_http_methods(['POST'])
def expense_create(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'errors': {'detail': 'Invalid JSON.'}}, status=400)

    errors = {}
    category = data.get('category', '').strip()
    amount = data.get('amount')
    expense_date = data.get('expense_date')

    if not category: errors['category'] = 'Category is required.'
    if not amount: errors['amount'] = 'Amount is required.'
    if not expense_date: errors['expense_date'] = 'Date is required.'

    if errors:
        return JsonResponse({'success': False, 'errors': errors}, status=400)

    expense = Expense.objects.create(
        landlord=request.user,
        category=category,
        amount=Decimal(str(amount)),
        expense_date=expense_date,
        description=data.get('description', ''),
    )
    return JsonResponse({'success': True, 'expense': {'id': expense.pk, 'amount': str(expense.amount)}}, status=201)
