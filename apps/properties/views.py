from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from apps.users.models import Landlord
from .models import Building, Property
import json


def landlord_dashboard_view(request):
    if request.session.get('user_role') != 'landlord':
        return redirect('/login/')

    try:
        landlord = Landlord.objects.get(pk=request.session.get('_auth_user_id'))
    except Landlord.DoesNotExist:
        return redirect('/login/')

    properties = Property.objects.filter(landlord=landlord)
    context = {
        'landlord': landlord,
        'properties_count': properties.count(),
        'properties': properties[:5],
    }
    return render(request, 'landlord/dashboard.html', context)


@require_http_methods(["GET"])
def properties_list_view(request):
    if request.session.get('user_role') != 'landlord':
        return redirect('/login/')

    try:
        landlord = Landlord.objects.get(pk=request.session.get('_auth_user_id'))
    except Landlord.DoesNotExist:
        return redirect('/login/')

    properties = Property.objects.filter(landlord=landlord)
    context = {
        'properties': properties,
        'landlord': landlord,
    }
    return render(request, 'landlord/properties_list.html', context)


@require_http_methods(["GET", "POST"])
@csrf_protect
def properties_create_view(request):
    if request.session.get('user_role') != 'landlord':
        return redirect('/login/')

    try:
        landlord = Landlord.objects.get(pk=request.session.get('_auth_user_id'))
    except Landlord.DoesNotExist:
        return redirect('/login/')

    if request.method == 'GET':
        buildings = Building.objects.filter(landlord=landlord)
        context = {'buildings': buildings}
        return render(request, 'landlord/properties_create.html', context)

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    unit_number = data.get('unit_number', '').strip()
    address = data.get('address', '').strip()
    property_type = data.get('property_type', 'apartment')
    rent_amount = data.get('rent_amount', 0)

    if not unit_number or not address:
        return JsonResponse({'error': 'Unit number and address are required'}, status=400)

    if Property.objects.filter(landlord=landlord, unit_number=unit_number).exists():
        return JsonResponse({'error': 'Unit number already exists'}, status=400)

    property_obj = Property.objects.create(
        landlord=landlord,
        unit_number=unit_number,
        address=address,
        property_type=property_type,
        rent_amount=rent_amount,
    )

    return JsonResponse({'success': True, 'property_id': str(property_obj.id)})


@require_http_methods(["GET"])
def properties_detail_view(request, property_id):
    if request.session.get('user_role') != 'landlord':
        return redirect('/login/')

    try:
        landlord = Landlord.objects.get(pk=request.session.get('_auth_user_id'))
    except Landlord.DoesNotExist:
        return redirect('/login/')

    property_obj = get_object_or_404(Property, id=property_id, landlord=landlord)
    context = {'property': property_obj}
    return render(request, 'landlord/properties_detail.html', context)


@require_http_methods(["GET", "POST"])
@csrf_protect
def properties_update_view(request, property_id):
    if request.session.get('user_role') != 'landlord':
        return redirect('/login/')

    try:
        landlord = Landlord.objects.get(pk=request.session.get('_auth_user_id'))
    except Landlord.DoesNotExist:
        return redirect('/login/')

    property_obj = get_object_or_404(Property, id=property_id, landlord=landlord)

    if request.method == 'GET':
        context = {'property': property_obj}
        return render(request, 'landlord/properties_update.html', context)

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    property_obj.address = data.get('address', property_obj.address)
    property_obj.property_type = data.get('property_type', property_obj.property_type)
    property_obj.rent_amount = data.get('rent_amount', property_obj.rent_amount)
    property_obj.status = data.get('status', property_obj.status)
    property_obj.description = data.get('description', property_obj.description)
    property_obj.save()

    return JsonResponse({'success': True})


@require_http_methods(["POST"])
@csrf_protect
def properties_delete_view(request, property_id):
    if request.session.get('user_role') != 'landlord':
        return redirect('/login/')

    try:
        landlord = Landlord.objects.get(pk=request.session.get('_auth_user_id'))
    except Landlord.DoesNotExist:
        return redirect('/login/')

    property_obj = get_object_or_404(Property, id=property_id, landlord=landlord)
    property_obj.delete()

    return JsonResponse({'success': True})
