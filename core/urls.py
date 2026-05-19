"""
Root URL Configuration — Rent & Lease Management System
Frontend HTML pages + JSON action endpoints for JS fetch calls.
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core import views as frontend_views
from apps.users import views as auth_views
from apps.properties import views as property_views
from apps.leases import views as lease_views
from apps.financials import views as financial_views

urlpatterns = [

    # ─── Public Pages ─────────────────────────────────────────
    path("", frontend_views.index_view, name="index"),
    path("login/", frontend_views.login_page, name="login_page"),
    path("register/", frontend_views.register_page, name="register_page"),
    path("forgot-password/", frontend_views.forgot_password_page, name="forgot_password_page"),
    path("reset-password/", frontend_views.reset_password_page, name="reset_password_page"),
    path("verify-email/", frontend_views.verify_email_page, name="verify_email_page"),
    path("payment/success/", frontend_views.payment_success, name="payment_success"),
    path("payment/cancelled/", frontend_views.payment_cancelled, name="payment_cancelled"),

    # ─── Auth Actions (POST — called by frontend JS via APIClient) ─────────
    path("api/v1/auth/register/", auth_views.register_view, name="auth_register"),
    path("api/v1/auth/login/", auth_views.login_view, name="auth_login"),
    path("api/v1/auth/logout/", auth_views.logout_view, name="auth_logout"),
    path("api/v1/auth/forgot-password/", auth_views.forgot_password_view, name="auth_forgot_password"),
    path("api/v1/auth/reset-password/", auth_views.reset_password_view, name="auth_reset_password"),

    # ─── Landlord Pages ───────────────────────────────────────
    path("landlord/dashboard/", frontend_views.landlord_dashboard, name="landlord_dashboard"),
    path("landlord/properties/", frontend_views.landlord_properties, name="landlord_properties"),
    path("landlord/leases/", frontend_views.landlord_leases, name="landlord_leases"),
    path("landlord/financials/", frontend_views.landlord_financials, name="landlord_financials"),
    path("landlord/tenants/", frontend_views.landlord_tenants, name="landlord_tenants"),
    path("landlord/maintenance/", frontend_views.landlord_maintenance, name="landlord_maintenance"),
    path("landlord/chat/", frontend_views.landlord_chat, name="landlord_chat"),
    path("landlord/documents/", frontend_views.landlord_documents, name="landlord_documents"),
    path("landlord/analytics/", frontend_views.landlord_analytics, name="landlord_analytics"),
    path("landlord/notifications/", frontend_views.landlord_notifications, name="landlord_notifications"),
    path("landlord/settings/", frontend_views.landlord_settings, name="landlord_settings"),
    path("landlord/automations/", frontend_views.landlord_automations, name="landlord_automations"),
    path("landlord/buildings/", frontend_views.landlord_buildings, name="landlord_buildings"),
    path("landlord/expenses/", frontend_views.landlord_expenses, name="landlord_expenses"),

    # ─── Tenant Pages ─────────────────────────────────────────
    path("tenant/dashboard/", frontend_views.tenant_dashboard, name="tenant_dashboard"),
    path("tenant/payments/", frontend_views.tenant_payments, name="tenant_payments"),
    path("tenant/lease/", frontend_views.tenant_lease, name="tenant_lease"),
    path("tenant/maintenance/", frontend_views.tenant_maintenance, name="tenant_maintenance"),
    path("tenant/chat/", frontend_views.tenant_chat, name="tenant_chat"),
    path("tenant/inspection/", frontend_views.tenant_inspection, name="tenant_inspection"),
    path("tenant/payment-methods/", frontend_views.tenant_payment_methods, name="tenant_payment_methods"),
    path("tenant/notice-board/", frontend_views.tenant_notice_board, name="tenant_notice_board"),
    path("tenant/compliance/", frontend_views.tenant_compliance, name="tenant_compliance"),
    path("tenant/profile/", frontend_views.tenant_profile, name="tenant_profile"),
    path("tenant/history/", frontend_views.tenant_history, name="tenant_history"),

    # ─── Properties API (JSON — called by frontend JS) ────────
    path("api/properties/", property_views.property_list, name="property_list"),
    path("api/properties/create/", property_views.property_create, name="property_create"),
    path("api/properties/<int:pk>/update/", property_views.property_update, name="property_update"),
    path("api/properties/<int:pk>/delete/", property_views.property_delete, name="property_delete"),
    path("api/buildings/", property_views.building_list, name="building_list"),
    path("api/buildings/create/", property_views.building_create, name="building_create"),

    # ─── Leases API (JSON — called by frontend JS) ────────────
    path("api/leases/", lease_views.lease_list, name="lease_list"),
    path("api/leases/create/", lease_views.lease_create, name="lease_create"),
    path("api/leases/expiring/", lease_views.lease_expiring, name="lease_expiring"),
    path("api/leases/<int:pk>/delete/", lease_views.lease_delete, name="lease_delete"),
    path("api/leases/<int:pk>/invite/", lease_views.lease_invite, name="lease_invite"),

    # ─── Financials API (JSON — called by frontend JS) ────────
    path("api/invoices/", financial_views.invoice_list, name="invoice_list"),
    path("api/invoices/create/", financial_views.invoice_create, name="invoice_create"),
    path("api/invoices/outstanding/", financial_views.invoice_outstanding, name="invoice_outstanding"),
    path("api/invoices/summary/", financial_views.invoice_summary, name="invoice_summary"),
    path("api/expenses/", financial_views.expense_list, name="expense_list"),
    path("api/expenses/create/", financial_views.expense_create, name="expense_create"),
    path("api/payments/pay/", financial_views.payment_pay, name="payment_pay"),

    # ─── Django Admin ─────────────────────────────────────────
    path("admin/", admin.site.urls),

]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Error handlers
handler403 = "core.views.error_403"
handler404 = "core.views.error_404"
handler429 = "core.views.error_429"
handler500 = "core.views.error_500"
