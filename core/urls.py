"""
Root URL Configuration — Rent & Lease Management System

All API endpoints are namespaced under /api/v1/.
WebSocket routes are handled by ASGI in core/asgi.py.
Frontend HTML views will be served from the root /.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views as frontend_views

urlpatterns = [
    # ─── Public Pages ────────────────────────────────────────────
    path("", frontend_views.index_view, name="index"),
    path("login/", frontend_views.login_page, name="login_page"),
    path("register/", frontend_views.register_page, name="register_page"),
    path(
        "forgot-password/",
        frontend_views.forgot_password_page,
        name="forgot_password_page",
    ),
    path(
        "reset-password/",
        frontend_views.reset_password_page,
        name="reset_password_page",
    ),
    path("verify-email/", frontend_views.verify_email_page, name="verify_email_page"),
    # Payment result pages
    path("payment/success/", frontend_views.payment_success, name="payment_success"),
    path(
        "payment/cancelled/", frontend_views.payment_cancelled, name="payment_cancelled"
    ),
    # ─── Landlord Pages ───────────────────────────────────────────
    path(
        "landlord/dashboard/",
        frontend_views.landlord_dashboard,
        name="landlord_dashboard",
    ),
    path(
        "landlord/properties/",
        frontend_views.landlord_properties,
        name="landlord_properties",
    ),
    path("landlord/leases/", frontend_views.landlord_leases, name="landlord_leases"),
    path(
        "landlord/financials/",
        frontend_views.landlord_financials,
        name="landlord_financials",
    ),
    path("landlord/tenants/", frontend_views.landlord_tenants, name="landlord_tenants"),
    path(
        "landlord/maintenance/",
        frontend_views.landlord_maintenance,
        name="landlord_maintenance",
    ),
    path("landlord/chat/", frontend_views.landlord_chat, name="landlord_chat"),
    path(
        "landlord/documents/",
        frontend_views.landlord_documents,
        name="landlord_documents",
    ),
    path(
        "landlord/analytics/",
        frontend_views.landlord_analytics,
        name="landlord_analytics",
    ),
    path(
        "landlord/notifications/",
        frontend_views.landlord_notifications,
        name="landlord_notifications",
    ),
    path(
        "landlord/settings/", frontend_views.landlord_settings, name="landlord_settings"
    ),
    path(
        "landlord/automations/",
        frontend_views.landlord_automations,
        name="landlord_automations",
    ),
    path(
        "landlord/buildings/",
        frontend_views.landlord_buildings,
        name="landlord_buildings",
    ),
    path(
        "landlord/expenses/", frontend_views.landlord_expenses, name="landlord_expenses"
    ),
    # ─── Tenant Pages ─────────────────────────────────────────────
    path("tenant/dashboard/", frontend_views.tenant_dashboard, name="tenant_dashboard"),
    path("tenant/payments/", frontend_views.tenant_payments, name="tenant_payments"),
    path("tenant/lease/", frontend_views.tenant_lease, name="tenant_lease"),
    path(
        "tenant/maintenance/",
        frontend_views.tenant_maintenance,
        name="tenant_maintenance",
    ),
    path("tenant/chat/", frontend_views.tenant_chat, name="tenant_chat"),
    path(
        "tenant/inspection/", frontend_views.tenant_inspection, name="tenant_inspection"
    ),
    path(
        "tenant/payment-methods/",
        frontend_views.tenant_payment_methods,
        name="tenant_payment_methods",
    ),
    path(
        "tenant/notice-board/",
        frontend_views.tenant_notice_board,
        name="tenant_notice_board",
    ),
    path(
        "tenant/compliance/", frontend_views.tenant_compliance, name="tenant_compliance"
    ),
    path("tenant/profile/", frontend_views.tenant_profile, name="tenant_profile"),
    path("tenant/history/", frontend_views.tenant_history, name="tenant_history"),
    # ─── Django Admin ─────────────────────────────────────────────
    path("admin/", admin.site.urls),
    # API v1 endpoints — activated as each app is built
    path('api/v1/auth/', include('apps.users.urls')),
    path('api/v1/properties/', include('apps.properties.urls')),
    path("api/v1/leases/", include("apps.leases.urls")),
    path("api/v1/financials/", include("apps.financials.urls")),
    # path("api/v1/maintenance/", include("apps.maintenance.urls")),
    # path("api/v1/chat/", include("apps.chat.urls")),
    # path("api/v1/documents/", include("apps.documents.urls")),
    # path("api/v1/analytics/", include("apps.analytics.urls")),
    # path("api/v1/notifications/", include("apps.notifications.urls")),
    # path("api/v1/automation/", include("apps.automation.urls")),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Error handlers
handler403 = "core.views.error_403"
handler404 = "core.views.error_404"
handler429 = "core.views.error_429"
handler500 = "core.views.error_500"
