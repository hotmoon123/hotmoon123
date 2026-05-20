"""
Root URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.users import views as user_views
from apps.properties import views as property_views
from apps.leases import views as lease_views
from apps.financials import views as financial_views
from apps.maintenance import views as maintenance_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', user_views.home_view, name='home'),

    # Authentication
    path('login/', user_views.login_view, name='login'),
    path('register/', user_views.register_view, name='register'),
    path('logout/', user_views.logout_view, name='logout'),

    # Landlord Dashboard & Properties
    path('landlord/dashboard/', property_views.landlord_dashboard_view, name='landlord_dashboard'),
    path('properties/list/', property_views.properties_list_view, name='properties_list'),
    path('properties/create/', property_views.properties_create_view, name='properties_create'),
    path('properties/<uuid:property_id>/detail/', property_views.properties_detail_view, name='properties_detail'),
    path('properties/<uuid:property_id>/update/', property_views.properties_update_view, name='properties_update'),
    path('properties/<uuid:property_id>/delete/', property_views.properties_delete_view, name='properties_delete'),

    # Leases
    path('leases/list/', lease_views.leases_list_view, name='leases_list'),
    path('leases/create/', lease_views.leases_create_view, name='leases_create'),
    path('leases/<uuid:lease_id>/detail/', lease_views.leases_detail_view, name='leases_detail'),
    path('leases/<uuid:lease_id>/sign/', lease_views.leases_sign_view, name='leases_sign'),

    # Financials
    path('invoices/list/', financial_views.invoices_list_view, name='invoices_list'),
    path('invoices/create/', financial_views.invoices_create_view, name='invoices_create'),
    path('invoices/<uuid:invoice_id>/pay/', financial_views.invoices_pay_view, name='invoices_pay'),
    path('expenses/list/', financial_views.expenses_list_view, name='expenses_list'),
    path('expenses/create/', financial_views.expenses_create_view, name='expenses_create'),

    # Maintenance
    path('maintenance/list/', maintenance_views.maintenance_list_view, name='maintenance_list'),
    path('maintenance/create/', maintenance_views.maintenance_create_view, name='maintenance_create'),
    path('maintenance/<uuid:ticket_id>/detail/', maintenance_views.maintenance_detail_view, name='maintenance_detail'),
    path('maintenance/<uuid:ticket_id>/update/', maintenance_views.maintenance_update_view, name='maintenance_update'),

    # Tenant Dashboard
    path('tenant/dashboard/', user_views.tenant_dashboard_view, name='tenant_dashboard'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
