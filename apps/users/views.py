"""
Users App — Django MVT Views (auth actions)
All form submissions are standard POST requests with CSRF.
"""
import json
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect

from .models import Landlord, Tenant
from .business_logic import (
    generate_password_reset_token,
    reset_password_with_token,
    send_password_reset_email,
)


@csrf_protect
@require_POST
def register_view(request):
    """POST /auth/register/ — creates landlord or tenant account."""
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        data = request.POST

    email = data.get('email', '').lower().strip()
    password = data.get('password', '')
    confirm_password = data.get('confirm_password', '')
    role = data.get('role', '')
    first_name = data.get('first_name', '').strip()
    last_name = data.get('last_name', '').strip()
    phone_number = data.get('phone_number', '').strip()

    errors = {}

    if not email:
        errors['email'] = 'Email is required.'
    elif Landlord.objects.filter(email=email).exists() or Tenant.objects.filter(email=email).exists():
        errors['email'] = 'An account with this email already exists.'

    if not password or len(password) < 8:
        errors['password'] = 'Password must be at least 8 characters.'
    elif password != confirm_password:
        errors['confirm_password'] = 'Passwords do not match.'

    if role not in ('landlord', 'tenant'):
        errors['role'] = 'Role must be landlord or tenant.'

    if not first_name:
        errors['first_name'] = 'First name is required.'
    if not last_name:
        errors['last_name'] = 'Last name is required.'

    if errors:
        return JsonResponse({'success': False, 'errors': errors}, status=400)

    if role == 'landlord':
        user = Landlord.objects.create_user(
            email=email, password=password,
            first_name=first_name, last_name=last_name,
            phone_number=phone_number,
        )
    else:
        user = Tenant.objects.create_user(
            email=email, password=password,
            first_name=first_name, last_name=last_name,
            phone_number=phone_number,
        )

    # Specify backend and store user type in session to resolve ID collisions
    login(request, user, backend='apps.users.auth_backend.EmailBackend')
    request.session['_auth_user_type'] = role
    redirect_url = '/landlord/dashboard/' if role == 'landlord' else '/tenant/dashboard/'
    return JsonResponse({'success': True, 'redirect': redirect_url})


@csrf_protect
@require_POST
def login_view(request):
    """POST /auth/login/ — authenticates and starts session."""
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        data = request.POST

    email = data.get('email', '').lower().strip()
    password = data.get('password', '')

    if not email or not password:
        return JsonResponse(
            {'success': False, 'errors': {'detail': 'Email and password are required.'}},
            status=400
        )

    user = authenticate(request, email=email, password=password)

    if not user:
        return JsonResponse(
            {'success': False, 'errors': {'detail': 'Invalid email or password.'}},
            status=401
        )

    login(request, user, backend='apps.users.auth_backend.EmailBackend')

    # Store user type in session to resolve ID collisions
    if isinstance(user, Landlord):
        request.session['_auth_user_type'] = 'landlord'
        redirect_url = '/landlord/dashboard/'
    elif isinstance(user, Tenant):
        request.session['_auth_user_type'] = 'tenant'
        redirect_url = '/tenant/dashboard/'
    else:
        redirect_url = '/'

    return JsonResponse({'success': True, 'redirect': redirect_url})


@require_POST
def logout_view(request):
    """POST /auth/logout/ — ends session."""
    logout(request)
    return JsonResponse({'success': True, 'redirect': '/login/'})


@csrf_protect
@require_POST
def forgot_password_view(request):
    """POST /auth/forgot-password/ — sends reset email (silent on unknown email)."""
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        data = request.POST

    email = data.get('email', '').lower().strip()

    if not email:
        return JsonResponse(
            {'success': False, 'errors': {'email': 'Email is required.'}},
            status=400
        )

    # Always return success — never reveal if email exists (anti-enumeration)
    user = None
    try:
        user = Landlord.objects.get(email=email)
    except Landlord.DoesNotExist:
        try:
            user = Tenant.objects.get(email=email)
        except Tenant.DoesNotExist:
            pass

    if user:
        try:
            raw_token = generate_password_reset_token(user)
            send_password_reset_email(user, raw_token)
        except Exception:
            pass

    return JsonResponse({
        'success': True,
        'message': 'If an account with that email exists, a reset link has been sent.'
    })


@csrf_protect
@require_POST
def reset_password_view(request):
    """POST /auth/reset-password/ — resets password using token."""
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        data = request.POST

    token = data.get('token', '').strip()
    new_password = data.get('new_password', '')
    confirm_password = data.get('confirm_password', '')

    errors = {}

    if not token:
        errors['token'] = 'Reset token is required.'
    if not new_password or len(new_password) < 8:
        errors['new_password'] = 'Password must be at least 8 characters.'
    elif new_password != confirm_password:
        errors['confirm_password'] = 'Passwords do not match.'

    if errors:
        return JsonResponse({'success': False, 'errors': errors}, status=400)

    user = reset_password_with_token(token, new_password)

    if not user:
        return JsonResponse(
            {'success': False, 'errors': {'detail': 'Invalid or expired reset link.'}},
            status=400
        )

    return JsonResponse({
        'success': True,
        'message': 'Password reset successfully. You can now log in.'
    })
