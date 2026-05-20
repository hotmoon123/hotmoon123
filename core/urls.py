"""
Root URL Configuration — RentFlow CRM Pure Django MVT Architecture
No middleware, no API routes, pure function-based views with view-level security.
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

    # ═══════════════════════════════════════════════════════════════
    # PUBLIC PAGES (Guest Access)
    # ═══════════════════════════════════════════════════════════════
    path('', user_views.home_view, name='home'),
    path('login/', user_views.login_view, name='login'),
    path('register/', user_views.register_view, name='register'),
    path('forgot-password/', user_views.forgot_password_view, name='forgot_password'),
    path('reset-password/', user_views.reset_password_view, name='reset_password'),
    path('logout/', user_views.logout_view, name='logout'),

    # ═══════════════════════════════════════════════════════════════
    # AUTHENTICATION ACTIONS (POST → JsonResponse)
    # ═══════════════════════════════════════════════════════════════
    path('auth/register/', user_views.register_view, name='auth_register'),
    path('auth/login/', user_views.login_view, name='auth_login'),
    path('auth/logout/', user_views.logout_view, name='auth_logout'),
    path('auth/forgot-password/', user_views.forgot_password_action_view, name='auth_forgot_password'),
    path('auth/reset-password/', user_views.reset_password_action_view, name='auth_reset_password'),

    # ═══════════════════════════════════════════════════════════════
    # LANDLORD DASHBOARD & PROPERTIES (Function-Based Views + View-Level Security)
    # ═══════════════════════════════════════════════════════════════
    path('landlord/dashboard/', property_views.landlord_dashboard_view, name='landlord_dashboard'),
    path('landlord/properties/', property_views.properties_list_view, name='landlord_properties'),
    path('landlord/buildings/', property_views.buildings_view, name='landlord_buildings'),
    path('landlord/leases/', lease_views.leases_landlord_view, name='landlord_leases'),
    path('landlord/tenants/', property_views.tenants_view, name='landlord_tenants'),
    path('landlord/financials/', financial_views.financials_view, name='landlord_financials'),
    path('landlord/maintenance/', maintenance_views.maintenance_landlord_view, name='landlord_maintenance'),
    path('landlord/chat/', property_views.chat_view, name='landlord_chat'),
    path('landlord/documents/', property_views.documents_view, name='landlord_documents'),
    path('landlord/analytics/', property_views.analytics_view, name='landlord_analytics'),
    path('landlord/notices/', property_views.notices_view, name='landlord_notices'),
    path('landlord/inspections/', property_views.inspections_view, name='landlord_inspections'),
    path('landlord/automations/', property_views.automations_view, name='landlord_automations'),
    path('landlord/settings/', property_views.settings_view, name='landlord_settings'),

    # ═══════════════════════════════════════════════════════════════
    # PROPERTIES (CRUD Operations)
    # ═══════════════════════════════════════════════════════════════
    path('properties/list/', property_views.properties_list_view, name='properties_list'),
    path('properties/create/', property_views.properties_create_view, name='properties_create'),
    path('properties/<uuid:property_id>/detail/', property_views.properties_detail_view, name='properties_detail'),
    path('properties/<uuid:property_id>/update/', property_views.properties_update_view, name='properties_update'),
    path('properties/<uuid:property_id>/delete/', property_views.properties_delete_view, name='properties_delete'),

    # ═══════════════════════════════════════════════════════════════
    # LEASES
    # ═══════════════════════════════════════════════════════════════
    path('leases/list/', lease_views.leases_list_view, name='leases_list'),
    path('leases/create/', lease_views.leases_create_view, name='leases_create'),
    path('leases/<uuid:lease_id>/detail/', lease_views.leases_detail_view, name='leases_detail'),
    path('leases/<uuid:lease_id>/sign/', lease_views.leases_sign_view, name='leases_sign'),
    path('leases/<uuid:lease_id>/invite/', lease_views.leases_invite_view, name='leases_invite'),

    # ═══════════════════════════════════════════════════════════════
    # FINANCIALS (Invoices, Expenses, Payments)
    # ═══════════════════════════════════════════════════════════════
    path('invoices/list/', financial_views.invoices_list_view, name='invoices_list'),
    path('invoices/create/', financial_views.invoices_create_view, name='invoices_create'),
    path('invoices/<uuid:invoice_id>/pay/', financial_views.invoices_pay_view, name='invoices_pay'),
    path('expenses/list/', financial_views.expenses_list_view, name='expenses_list'),
    path('expenses/create/', financial_views.expenses_create_view, name='expenses_create'),
    path('payments/process-momo/', financial_views.process_momo_payment, name='process_momo'),

    # ═══════════════════════════════════════════════════════════════
    # MAINTENANCE
    # ═══════════════════════════════════════════════════════════════
    path('maintenance/list/', maintenance_views.maintenance_list_view, name='maintenance_list'),
    path('maintenance/create/', maintenance_views.maintenance_create_view, name='maintenance_create'),
    path('maintenance/<uuid:ticket_id>/detail/', maintenance_views.maintenance_detail_view, name='maintenance_detail'),
    path('maintenance/<uuid:ticket_id>/update/', maintenance_views.maintenance_update_view, name='maintenance_update'),

    # ═══════════════════════════════════════════════════════════════
    # TENANT DASHBOARD
    # ═══════════════════════════════════════════════════════════════
    path('tenant/dashboard/', user_views.tenant_dashboard_view, name='tenant_dashboard'),
    path('tenant/payments/', user_views.tenant_payments_view, name='tenant_payments'),
    path('tenant/lease/', user_views.tenant_lease_view, name='tenant_lease'),
    path('tenant/maintenance/', maintenance_views.maintenance_tenant_view, name='tenant_maintenance'),
    path('tenant/chat/', user_views.tenant_chat_view, name='tenant_chat'),
    path('tenant/notice-board/', user_views.tenant_notice_board_view, name='tenant_notice_board'),
    path('tenant/compliance/', user_views.tenant_compliance_view, name='tenant_compliance'),
    path('tenant/payment-methods/', user_views.tenant_payment_methods_view, name='tenant_payment_methods'),
    path('tenant/profile/', user_views.tenant_profile_view, name='tenant_profile'),
    path('tenant/history/', user_views.tenant_history_view, name='tenant_history'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
