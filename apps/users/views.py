from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from .models import Landlord, Tenant
import json


@require_http_methods(["GET", "POST"])
@csrf_protect
def register_view(request):
    if request.method == 'GET':
        return render(request, 'auth/register.html')

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    user_type = data.get('user_type', '').lower()
    email = data.get('email', '').strip()
    password = data.get('password', '')
    password_confirm = data.get('password_confirm', '')
    first_name = data.get('first_name', '').strip()
    last_name = data.get('last_name', '').strip()

    if not email or not password or not user_type:
        return JsonResponse({'error': 'Email, password, and user type are required'}, status=400)

    if password != password_confirm:
        return JsonResponse({'error': 'Passwords do not match'}, status=400)

    if user_type == 'landlord':
        if Landlord.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already registered'}, status=400)
        user = Landlord.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
    elif user_type == 'tenant':
        if Tenant.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already registered'}, status=400)
        user = Tenant.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
    else:
        return JsonResponse({'error': 'Invalid user type'}, status=400)

    login(request, user, backend='apps.users.auth_backend.EmailBackend')
    request.session['user_role'] = user_type

    return JsonResponse({'success': True, 'redirect': f'/{user_type}/dashboard/'})


@require_http_methods(["GET", "POST"])
@csrf_protect
def login_view(request):
    if request.method == 'GET':
        return render(request, 'auth/login.html')

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    email = data.get('email', '').strip()
    password = data.get('password', '')

    if not email or not password:
        return JsonResponse({'error': 'Email and password are required'}, status=400)

    user = authenticate(request, email=email, password=password)

    if user is None:
        return JsonResponse({'error': 'Invalid email or password'}, status=401)

    login(request, user, backend='apps.users.auth_backend.EmailBackend')

    if isinstance(user, Landlord):
        request.session['user_role'] = 'landlord'
        return JsonResponse({'success': True, 'redirect': '/landlord/dashboard/'})
    elif isinstance(user, Tenant):
        request.session['user_role'] = 'tenant'
        return JsonResponse({'success': True, 'redirect': '/tenant/dashboard/'})

    return JsonResponse({'error': 'Unknown user type'}, status=500)


def logout_view(request):
    logout(request)
    return redirect('/login/')


def home_view(request):
    if 'user_role' in request.session:
        user_type = request.session['user_role']
        return redirect(f'/{user_type}/dashboard/')
    return render(request, 'home.html')


def tenant_dashboard_view(request):
    if request.session.get('user_role') != 'tenant':
        return redirect('/login/')

    try:
        tenant = Tenant.objects.get(pk=request.session.get('_auth_user_id'))
    except Tenant.DoesNotExist:
        return redirect('/login/')

    from apps.leases.models import Lease
    from apps.financials.models import Invoice

    leases = Lease.objects.filter(tenant=tenant)
    invoices = Invoice.objects.filter(tenant=tenant)

    context = {
        'tenant': tenant,
        'leases_count': leases.count(),
        'leases': leases,
        'unpaid_invoices': invoices.filter(status__in=['unpaid', 'overdue']),
    }
    return render(request, 'tenant/dashboard.html', context)
