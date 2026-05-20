from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from apps.users.models import Landlord, Tenant
from apps.properties.models import Property
from .models import MaintenanceTicket
import json


@require_http_methods(["GET"])
def maintenance_list_view(request):
    if request.session.get('user_role') not in ['landlord', 'tenant']:
        return redirect('/login/')

    user_type = request.session.get('user_role')
    if user_type == 'landlord':
        try:
            landlord = Landlord.objects.get(pk=request.session.get('_auth_user_id'))
        except Landlord.DoesNotExist:
            return redirect('/login/')
        tickets = MaintenanceTicket.objects.filter(landlord=landlord)
    else:
        try:
            tenant = Tenant.objects.get(pk=request.session.get('_auth_user_id'))
        except Tenant.DoesNotExist:
            return redirect('/login/')
        tickets = MaintenanceTicket.objects.filter(tenant=tenant)

    context = {'tickets': tickets}
    return render(request, 'maintenance/maintenance_list.html', context)


@require_http_methods(["GET", "POST"])
@csrf_protect
def maintenance_create_view(request):
    if request.session.get('user_role') != 'tenant':
        return redirect('/login/')

    try:
        tenant = Tenant.objects.get(pk=request.session.get('_auth_user_id'))
    except Tenant.DoesNotExist:
        return redirect('/login/')

    if request.method == 'GET':
        from apps.leases.models import Lease
        leases = Lease.objects.filter(tenant=tenant)
        context = {'leases': leases}
        return render(request, 'maintenance/maintenance_create.html', context)

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    property_id = data.get('property_id')
    title = data.get('title')
    description = data.get('description')
    priority = data.get('priority', 'medium')

    if not property_id or not title or not description:
        return JsonResponse({'error': 'Missing required fields'}, status=400)

    try:
        from apps.leases.models import Lease
        lease = Lease.objects.get(tenant=tenant)
        property_obj = lease.property
    except:
        return JsonResponse({'error': 'Property not found'}, status=404)

    try:
        landlord = property_obj.landlord
    except:
        return JsonResponse({'error': 'Landlord not found'}, status=404)

    ticket = MaintenanceTicket.objects.create(
        landlord=landlord,
        tenant=tenant,
        property=property_obj,
        title=title,
        description=description,
        priority=priority,
    )

    return JsonResponse({'success': True, 'ticket_id': str(ticket.id)})


@require_http_methods(["GET"])
def maintenance_detail_view(request, ticket_id):
    if request.session.get('user_role') not in ['landlord', 'tenant']:
        return redirect('/login/')

    user_type = request.session.get('user_role')
    if user_type == 'landlord':
        try:
            landlord = Landlord.objects.get(pk=request.session.get('_auth_user_id'))
        except Landlord.DoesNotExist:
            return redirect('/login/')
        ticket = get_object_or_404(MaintenanceTicket, id=ticket_id, landlord=landlord)
    else:
        try:
            tenant = Tenant.objects.get(pk=request.session.get('_auth_user_id'))
        except Tenant.DoesNotExist:
            return redirect('/login/')
        ticket = get_object_or_404(MaintenanceTicket, id=ticket_id, tenant=tenant)

    context = {'ticket': ticket}
    return render(request, 'maintenance/maintenance_detail.html', context)


@require_http_methods(["POST"])
@csrf_protect
def maintenance_update_view(request, ticket_id):
    if request.session.get('user_role') != 'landlord':
        return redirect('/login/')

    try:
        landlord = Landlord.objects.get(pk=request.session.get('_auth_user_id'))
    except Landlord.DoesNotExist:
        return redirect('/login/')

    ticket = get_object_or_404(MaintenanceTicket, id=ticket_id, landlord=landlord)

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    ticket.status = data.get('status', ticket.status)
    ticket.priority = data.get('priority', ticket.priority)
    ticket.estimated_cost = data.get('estimated_cost', ticket.estimated_cost)
    ticket.save()

    return JsonResponse({'success': True})
