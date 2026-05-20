from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone
from apps.users.models import Landlord, Tenant
from apps.properties.models import Property
from .models import Lease, Invitation
import json


@require_http_methods(["GET"])
def leases_list_view(request):
    if request.session.get('user_role') not in ['landlord', 'tenant']:
        return redirect('/login/')

    user_type = request.session.get('user_role')
    if user_type == 'landlord':
        try:
            landlord = Landlord.objects.get(pk=request.session.get('_auth_user_id'))
        except Landlord.DoesNotExist:
            return redirect('/login/')
        leases = Lease.objects.filter(landlord=landlord)
    else:
        try:
            tenant = Tenant.objects.get(pk=request.session.get('_auth_user_id'))
        except Tenant.DoesNotExist:
            return redirect('/login/')
        leases = Lease.objects.filter(tenant=tenant)

    context = {'leases': leases}
    return render(request, 'leases/leases_list.html', context)


@require_http_methods(["GET", "POST"])
@csrf_protect
def leases_create_view(request):
    if request.session.get('user_role') != 'landlord':
        return redirect('/login/')

    try:
        landlord = Landlord.objects.get(pk=request.session.get('_auth_user_id'))
    except Landlord.DoesNotExist:
        return redirect('/login/')

    if request.method == 'GET':
        properties = Property.objects.filter(landlord=landlord)
        context = {'properties': properties}
        return render(request, 'leases/leases_create.html', context)

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    property_id = data.get('property_id')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    rent_amount = data.get('rent_amount')
    deposit_amount = data.get('deposit_amount', 0)

    if not property_id or not start_date or not end_date or not rent_amount:
        return JsonResponse({'error': 'Missing required fields'}, status=400)

    try:
        property_obj = Property.objects.get(id=property_id, landlord=landlord)
    except Property.DoesNotExist:
        return JsonResponse({'error': 'Property not found'}, status=404)

    lease = Lease.objects.create(
        landlord=landlord,
        property=property_obj,
        start_date=start_date,
        end_date=end_date,
        rent_amount=rent_amount,
        deposit_amount=deposit_amount,
    )

    return JsonResponse({'success': True, 'lease_id': str(lease.id)})


@require_http_methods(["GET"])
def leases_detail_view(request, lease_id):
    if request.session.get('user_role') not in ['landlord', 'tenant']:
        return redirect('/login/')

    user_type = request.session.get('user_role')
    if user_type == 'landlord':
        try:
            landlord = Landlord.objects.get(pk=request.session.get('_auth_user_id'))
        except Landlord.DoesNotExist:
            return redirect('/login/')
        lease = get_object_or_404(Lease, id=lease_id, landlord=landlord)
    else:
        try:
            tenant = Tenant.objects.get(pk=request.session.get('_auth_user_id'))
        except Tenant.DoesNotExist:
            return redirect('/login/')
        lease = get_object_or_404(Lease, id=lease_id, tenant=tenant)

    context = {'lease': lease}
    return render(request, 'leases/leases_detail.html', context)


@require_http_methods(["POST"])
@csrf_protect
def leases_sign_view(request, lease_id):
    if request.session.get('user_role') != 'tenant':
        return redirect('/login/')

    try:
        tenant = Tenant.objects.get(pk=request.session.get('_auth_user_id'))
    except Tenant.DoesNotExist:
        return redirect('/login/')

    lease = get_object_or_404(Lease, id=lease_id, tenant=tenant)
    lease.status = 'active'
    lease.signed_at = timezone.now()
    lease.save()

    return JsonResponse({'success': True})


@require_http_methods(["GET"])
def leases_landlord_view(request):
    if request.session.get('user_role') != 'landlord':
        return redirect('/login/')

    try:
        landlord = Landlord.objects.get(pk=request.session.get('_auth_user_id'))
    except Landlord.DoesNotExist:
        return redirect('/login/')

    leases = Lease.objects.filter(landlord=landlord)
    context = {'leases': leases, 'landlord': landlord}
    return render(request, 'landlord/leases.html', context)


@require_http_methods(["POST"])
@csrf_protect
def leases_invite_view(request, lease_id):
    if request.session.get('user_role') != 'landlord':
        return redirect('/login/')

    try:
        landlord = Landlord.objects.get(pk=request.session.get('_auth_user_id'))
    except Landlord.DoesNotExist:
        return redirect('/login/')

    lease = get_object_or_404(Lease, id=lease_id, landlord=landlord)

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    email = data.get('email', '').strip()

    if not email:
        return JsonResponse({'error': 'Email is required'}, status=400)

    # Create invitation token
    import secrets
    token = secrets.token_urlsafe(32)

    invitation = Invitation.objects.create(
        lease=lease,
        landlord=landlord,
        email=email,
        token_hash=token,
        expires_at=timezone.now() + timezone.timedelta(days=7)
    )

    return JsonResponse({'success': True, 'invitation_id': str(invitation.id)})
