"""
Properties App — Django MVT Views
Returns JSON for AJAX calls from the frontend JS.
"""
import json
from decimal import Decimal
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.db.models import Exists, OuterRef, Sum, Value
from django.db.models.functions import Coalesce

from apps.leases.models import Lease
from .models import Building, Property


def property_to_dict(prop):
    return {
        'id': prop.pk,
        'unit_number': prop.unit_number,
        'address': getattr(prop, 'address', ''),
        'type': prop.type,
        'rent_amount': str(prop.rent_amount),
        'status': prop.status,
        'building_id': prop.building_id,
        'building_name': prop.building.name if prop.building else None,
        'has_active_lease': getattr(prop, 'has_active_lease', False),
        'created_at': prop.created_at.isoformat(),
    }


@login_required
@require_http_methods(['GET'])
def property_list(request):
    active_lease = Lease.objects.filter(
        property_id=OuterRef('pk'), status='active', deleted_at__isnull=True
    )
    qs = (
        Property.objects.filter(landlord=request.user)
        .select_related('building')
        .annotate(has_active_lease=Exists(active_lease))
        .order_by('-created_at')
    )
    total = qs.count()
    occupied = qs.filter(status='occupied').count()
    monthly = qs.aggregate(
        m=Coalesce(Sum('rent_amount'), Value(Decimal('0.00')))
    )['m']
    return JsonResponse({
        'summary': {
            'total_units': total,
            'occupied_units': occupied,
            'vacant_units': total - occupied,
            'monthly_rent_potential': str(monthly),
        },
        'results': [property_to_dict(p) for p in qs],
    })


@login_required
@require_http_methods(['POST'])
def property_create(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'errors': {'detail': 'Invalid JSON.'}}, status=400)

    errors = {}
    unit_number = data.get('unit_number', '').strip()
    rent_amount = data.get('rent_amount')
    prop_type = data.get('type', '').strip()

    if not unit_number:
        errors['unit_number'] = 'Unit number is required.'
    if not rent_amount:
        errors['rent_amount'] = 'Rent amount is required.'
    if not prop_type:
        errors['type'] = 'Property type is required.'

    if errors:
        return JsonResponse({'success': False, 'errors': errors}, status=400)

    building_id = data.get('building_id')
    building = None
    if building_id:
        try:
            building = Building.objects.get(pk=building_id, landlord=request.user)
        except Building.DoesNotExist:
            return JsonResponse({'success': False, 'errors': {'building_id': 'Building not found.'}}, status=400)

    prop = Property.objects.create(
        landlord=request.user,
        unit_number=unit_number,
        rent_amount=Decimal(str(rent_amount)),
        type=prop_type,
        building=building,
        address=data.get('address', ''),
        status=data.get('status', 'vacant'),
    )
    return JsonResponse({'success': True, 'property': property_to_dict(prop)}, status=201)


@login_required
@require_http_methods(['PUT', 'PATCH'])
def property_update(request, pk):
    try:
        prop = Property.objects.get(pk=pk, landlord=request.user)
    except Property.DoesNotExist:
        return JsonResponse({'success': False, 'errors': {'detail': 'Not found.'}}, status=404)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'errors': {'detail': 'Invalid JSON.'}}, status=400)

    for field in ('unit_number', 'address', 'type', 'status'):
        if field in data:
            setattr(prop, field, data[field])
    if 'rent_amount' in data:
        prop.rent_amount = Decimal(str(data['rent_amount']))
    prop.save()
    return JsonResponse({'success': True, 'property': property_to_dict(prop)})


@login_required
@require_http_methods(['DELETE'])
def property_delete(request, pk):
    try:
        prop = Property.objects.get(pk=pk, landlord=request.user)
    except Property.DoesNotExist:
        return JsonResponse({'success': False, 'errors': {'detail': 'Not found.'}}, status=404)

    if Lease.objects.filter(property=prop, status='active', deleted_at__isnull=True).exists():
        return JsonResponse(
            {'success': False, 'errors': {'detail': 'Cannot delete a property with an active lease.'}},
            status=400
        )
    prop.delete()
    return JsonResponse({'success': True})


@login_required
@require_http_methods(['GET'])
def building_list(request):
    buildings = Building.objects.filter(landlord=request.user).order_by('name')
    return JsonResponse({'results': [
        {'id': b.pk, 'name': b.name, 'address': getattr(b, 'address', '')}
        for b in buildings
    ]})


@login_required
@require_http_methods(['POST'])
def building_create(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'errors': {'detail': 'Invalid JSON.'}}, status=400)

    name = data.get('name', '').strip()
    if not name:
        return JsonResponse({'success': False, 'errors': {'name': 'Name is required.'}}, status=400)

    building = Building.objects.create(
        landlord=request.user,
        name=name,
        address=data.get('address', ''),
        description=data.get('description', ''),
    )
    return JsonResponse({'success': True, 'building': {'id': building.pk, 'name': building.name}}, status=201)
