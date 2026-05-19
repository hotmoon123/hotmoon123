"""
Leases App — Django MVT Views
Returns JSON for AJAX calls from the frontend JS.
"""
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.utils import timezone

from apps.users.models import Landlord
from .models import Lease, Invitation


def lease_to_dict(lease):
    return {
        'id': lease.pk,
        'property_id': lease.property_id,
        'property_unit': lease.property.unit_number if lease.property else None,
        'tenant_id': lease.tenant_id,
        'tenant_name': (
            f"{lease.tenant.first_name} {lease.tenant.last_name}".strip()
            if lease.tenant else None
        ),
        'start_date': lease.start_date.isoformat() if lease.start_date else None,
        'end_date': lease.end_date.isoformat() if lease.end_date else None,
        'rent_amount': str(lease.rent_amount),
        'status': lease.status,
    }


@login_required
@require_http_methods(['GET'])
def lease_list(request):
    user = request.user
    if isinstance(user, Landlord):
        qs = Lease.objects.filter(landlord=user, deleted_at__isnull=True).select_related('property', 'tenant')
    else:
        qs = Lease.objects.filter(tenant=user, deleted_at__isnull=True).select_related('property', 'landlord')
    return JsonResponse({'results': [lease_to_dict(l) for l in qs]})


@login_required
@require_http_methods(['POST'])
def lease_create(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'errors': {'detail': 'Invalid JSON.'}}, status=400)

    from apps.properties.models import Property
    errors = {}
    property_id = data.get('property_id')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    rent_amount = data.get('rent_amount')

    if not property_id: errors['property_id'] = 'Property is required.'
    if not start_date: errors['start_date'] = 'Start date is required.'
    if not end_date: errors['end_date'] = 'End date is required.'
    if not rent_amount: errors['rent_amount'] = 'Rent amount is required.'

    if errors:
        return JsonResponse({'success': False, 'errors': errors}, status=400)

    try:
        prop = Property.objects.get(pk=property_id, landlord=request.user)
    except Property.DoesNotExist:
        return JsonResponse({'success': False, 'errors': {'property_id': 'Property not found.'}}, status=404)

    lease = Lease.objects.create(
        landlord=request.user,
        property=prop,
        start_date=start_date,
        end_date=end_date,
        rent_amount=rent_amount,
        status='active',
    )
    return JsonResponse({'success': True, 'lease': lease_to_dict(lease)}, status=201)


@login_required
@require_http_methods(['DELETE'])
def lease_delete(request, pk):
    try:
        lease = Lease.objects.get(pk=pk, landlord=request.user, deleted_at__isnull=True)
    except Lease.DoesNotExist:
        return JsonResponse({'success': False, 'errors': {'detail': 'Not found.'}}, status=404)
    lease.deleted_at = timezone.now()
    lease.save()
    return JsonResponse({'success': True})


@login_required
@require_http_methods(['GET'])
def lease_expiring(request):
    days = int(request.GET.get('days', 60))
    target = timezone.now().date() + timezone.timedelta(days=days)
    qs = Lease.objects.filter(
        landlord=request.user,
        status='active',
        end_date__lte=target,
        end_date__gte=timezone.now().date(),
        deleted_at__isnull=True,
    ).select_related('property', 'tenant').order_by('end_date')
    return JsonResponse({'results': [lease_to_dict(l) for l in qs]})


@login_required
@require_http_methods(['POST'])
def lease_invite(request, pk):
    try:
        lease = Lease.objects.get(pk=pk, landlord=request.user, deleted_at__isnull=True)
    except Lease.DoesNotExist:
        return JsonResponse({'success': False, 'errors': {'detail': 'Not found.'}}, status=404)

    if lease.tenant:
        return JsonResponse({'success': False, 'errors': {'detail': 'Lease already has a tenant.'}}, status=400)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'errors': {'detail': 'Invalid JSON.'}}, status=400)

    email = data.get('email', '').strip()
    if not email:
        return JsonResponse({'success': False, 'errors': {'email': 'Email is required.'}}, status=400)

    import hashlib, secrets
    raw_token = secrets.token_urlsafe(32)
    token_hash = hashlib.sha256(raw_token.encode()).hexdigest()

    Invitation.objects.create(
        lease=lease,
        landlord=request.user,
        email=email,
        token_hash=token_hash,
        expires_at=timezone.now() + timezone.timedelta(hours=24),
    )
    return JsonResponse({'success': True, 'message': f'Invitation sent to {email}.'}, status=201)
