from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone
from apps.users.models import Landlord, Tenant
from apps.leases.models import Lease
from apps.properties.models import Property
from .models import Invoice, Transaction, Expense, PaymentMethod
import json
from decimal import Decimal


@require_http_methods(["GET"])
def invoices_list_view(request):
    if request.session.get('user_role') not in ['landlord', 'tenant']:
        return redirect('/login/')

    user_type = request.session.get('user_role')
    if user_type == 'landlord':
        try:
            landlord = Landlord.objects.get(pk=request.session.get('_auth_user_id'))
        except Landlord.DoesNotExist:
            return redirect('/login/')
        invoices = Invoice.objects.filter(landlord=landlord)
    else:
        try:
            tenant = Tenant.objects.get(pk=request.session.get('_auth_user_id'))
        except Tenant.DoesNotExist:
            return redirect('/login/')
        invoices = Invoice.objects.filter(tenant=tenant)

    context = {'invoices': invoices}
    return render(request, 'financials/invoices_list.html', context)


@require_http_methods(["GET", "POST"])
@csrf_protect
def invoices_create_view(request):
    if request.session.get('user_role') != 'landlord':
        return redirect('/login/')

    try:
        landlord = Landlord.objects.get(pk=request.session.get('_auth_user_id'))
    except Landlord.DoesNotExist:
        return redirect('/login/')

    if request.method == 'GET':
        leases = Lease.objects.filter(landlord=landlord)
        context = {'leases': leases}
        return render(request, 'financials/invoices_create.html', context)

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    lease_id = data.get('lease_id')
    amount = data.get('amount')
    due_date = data.get('due_date')
    invoice_type = data.get('invoice_type', 'rent')

    if not lease_id or not amount or not due_date:
        return JsonResponse({'error': 'Missing required fields'}, status=400)

    try:
        lease = Lease.objects.get(id=lease_id, landlord=landlord)
    except Lease.DoesNotExist:
        return JsonResponse({'error': 'Lease not found'}, status=404)

    if not lease.tenant:
        return JsonResponse({'error': 'Lease has no tenant'}, status=400)

    invoice = Invoice.objects.create(
        landlord=landlord,
        tenant=lease.tenant,
        lease=lease,
        rental_property=lease.property,
        amount=Decimal(str(amount)),
        due_date=due_date,
        invoice_type=invoice_type,
    )

    return JsonResponse({'success': True, 'invoice_id': str(invoice.id)})


@require_http_methods(["POST"])
@csrf_protect
def invoices_pay_view(request, invoice_id):
    if request.session.get('user_role') != 'tenant':
        return redirect('/login/')

    try:
        tenant = Tenant.objects.get(pk=request.session.get('_auth_user_id'))
    except Tenant.DoesNotExist:
        return redirect('/login/')

    invoice = get_object_or_404(Invoice, id=invoice_id, tenant=tenant)

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    amount = Decimal(str(data.get('amount', invoice.balance_due)))
    momo_provider = data.get('momo_provider', 'mtn')
    momo_number = data.get('momo_number', '')

    if amount <= 0 or amount > invoice.balance_due:
        return JsonResponse({'error': 'Invalid amount'}, status=400)

    transaction = Transaction.objects.create(
        invoice=invoice,
        tenant=tenant,
        landlord=invoice.landlord,
        amount=amount,
        momo_provider=momo_provider,
        momo_number=momo_number,
        idempotency_key=f"{invoice.id}_{timezone.now().isoformat()}",
    )

    invoice.amount_paid += amount
    if invoice.amount_paid >= invoice.amount:
        invoice.status = 'paid'
        invoice.paid_at = timezone.now()
    elif invoice.amount_paid > 0:
        invoice.status = 'partial'
    invoice.save()

    return JsonResponse({'success': True, 'transaction_id': str(transaction.id)})


@require_http_methods(["GET"])
def expenses_list_view(request):
    if request.session.get('user_role') != 'landlord':
        return redirect('/login/')

    try:
        landlord = Landlord.objects.get(pk=request.session.get('_auth_user_id'))
    except Landlord.DoesNotExist:
        return redirect('/login/')

    expenses = Expense.objects.filter(landlord=landlord)
    context = {'expenses': expenses}
    return render(request, 'financials/expenses_list.html', context)


@require_http_methods(["GET", "POST"])
@csrf_protect
def expenses_create_view(request):
    if request.session.get('user_role') != 'landlord':
        return redirect('/login/')

    try:
        landlord = Landlord.objects.get(pk=request.session.get('_auth_user_id'))
    except Landlord.DoesNotExist:
        return redirect('/login/')

    if request.method == 'GET':
        properties = Property.objects.filter(landlord=landlord)
        context = {'properties': properties}
        return render(request, 'financials/expenses_create.html', context)

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    category = data.get('category')
    amount = data.get('amount')
    description = data.get('description')
    expense_date = data.get('expense_date')

    if not category or not amount or not description or not expense_date:
        return JsonResponse({'error': 'Missing required fields'}, status=400)

    expense = Expense.objects.create(
        landlord=landlord,
        category=category,
        amount=Decimal(str(amount)),
        description=description,
        expense_date=expense_date,
    )

    return JsonResponse({'success': True, 'expense_id': str(expense.id)})


@require_http_methods(["GET"])
def financials_view(request):
    if request.session.get('user_role') != 'landlord':
        return redirect('/login/')

    try:
        landlord = Landlord.objects.get(pk=request.session.get('_auth_user_id'))
    except Landlord.DoesNotExist:
        return redirect('/login/')

    invoices = Invoice.objects.filter(landlord=landlord)
    expenses = Expense.objects.filter(landlord=landlord)

    context = {
        'landlord': landlord,
        'invoices': invoices,
        'expenses': expenses,
        'total_revenue': sum(inv.amount for inv in invoices),
        'total_expenses': sum(exp.amount for exp in expenses),
    }
    return render(request, 'landlord/financials.html', context)


@require_http_methods(["POST"])
@csrf_protect
def process_momo_payment(request):
    if request.session.get('user_role') != 'tenant':
        return redirect('/login/')

    try:
        tenant = Tenant.objects.get(pk=request.session.get('_auth_user_id'))
    except Tenant.DoesNotExist:
        return redirect('/login/')

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    phone_number = data.get('phone_number', '').strip()
    amount = data.get('amount')
    provider = data.get('provider', 'mtn')

    if not phone_number or not amount:
        return JsonResponse({'error': 'Phone number and amount are required'}, status=400)

    # TODO: Integrate with actual MoMo payment gateway (MTN, Telecel, Vodafone)
    return JsonResponse({'success': True, 'message': 'Payment initiated'})
