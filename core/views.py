from django.shortcuts import render


def index_view(request):
    """Public marketing landing page."""
    return render(request, "public/landing.html")


def login_page(request):
    """Login page for all users."""
    return render(request, "public/login.html")


def register_page(request):
    """Registration page for all users."""
    return render(request, "public/register.html")


def forgot_password_page(request):
    """Forgot password page."""
    return render(request, "public/forgot_password.html")


def reset_password_page(request):
    """Reset password page."""
    return render(request, "public/reset_password.html")


def verify_email_page(request):
    """Email verification page."""
    return render(request, "public/verify_email.html")


# ─── Landlord Pages ────────────────────────────────────────────


def landlord_dashboard(request):
    """Landlord dashboard with portfolio overview."""
    return render(request, "landlord/dashboard.html")


def landlord_properties(request):
    """Property portfolio management."""
    return render(request, "landlord/properties.html")


def landlord_leases(request):
    """Lease management page."""
    return render(request, "landlord/leases.html")


def landlord_financials(request):
    """Financial management page."""
    return render(request, "landlord/financials.html")


def landlord_tenants(request):
    """Tenant directory page."""
    return render(request, "landlord/tenants.html")


def landlord_maintenance(request):
    """Maintenance kanban board."""
    return render(request, "landlord/maintenance.html")


def landlord_chat(request):
    """Real-time chat page."""
    return render(request, "landlord/chat.html")


def landlord_documents(request):
    """Document management page."""
    return render(request, "landlord/documents.html")


def landlord_analytics(request):
    """Analytics and reporting page."""
    return render(request, "landlord/analytics.html")


def landlord_notifications(request):
    """Notification center page."""
    return render(request, "landlord/notifications.html")


def landlord_settings(request):
    """Settings and profile page."""
    return render(request, "landlord/settings.html")


def landlord_automations(request):
    """Automation control panel page."""
    return render(request, "landlord/automations.html")


def landlord_buildings(request):
    """Multi-unit building management page."""
    return render(request, "landlord/buildings.html")


def landlord_expenses(request):
    """Expense and ROI ledger page."""
    return render(request, "landlord/expenses.html")


# ─── Tenant Pages ─────────────────────────────────────────────


def tenant_dashboard(request):
    """Tenant dashboard with balance overview."""
    return render(request, "tenant/dashboard.html")


def tenant_payments(request):
    """Rent payment page."""
    return render(request, "tenant/payments.html")


def tenant_lease(request):
    """Lease details page."""
    return render(request, "tenant/lease.html")


def tenant_maintenance(request):
    """Maintenance ticket submission page."""
    return render(request, "tenant/maintenance.html")


def tenant_chat(request):
    """Chat with landlord page."""
    return render(request, "tenant/chat.html")


def tenant_inspection(request):
    """Move-in/move-out inspection page."""
    return render(request, "tenant/inspection.html")


def tenant_payment_methods(request):
    """Payment methods management page."""
    return render(request, "tenant/payment_methods.html")


def tenant_notice_board(request):
    """Landlord notice board page."""
    return render(request, "tenant/notice_board.html")


def tenant_compliance(request):
    """Compliance documents page."""
    return render(request, "tenant/compliance.html")


def tenant_profile(request):
    """Profile settings page."""
    return render(request, "tenant/profile.html")


def tenant_history(request):
    """Payment history page."""
    return render(request, "tenant/history.html")


# ─── Public Pages ─────────────────────────────────────────────


def payment_success(request):
    """Payment success page."""
    return render(request, "public/payment_success.html")


def payment_cancelled(request):
    """Payment cancelled page."""
    return render(request, "public/payment_cancelled.html")


def error_403(request, exception):
    """403 Forbidden page."""
    return render(
        request,
        "public/error_generic.html",
        {
            "error_code": "403",
            "error_title": "Forbidden",
            "error_message": "You do not have permission to access this resource.",
        },
        status=403,
    )


def error_404(request, exception):
    """404 Not Found page."""
    return render(
        request,
        "public/error_generic.html",
        {
            "error_code": "404",
            "error_title": "Page Not Found",
            "error_message": "The page you requested does not exist.",
        },
        status=404,
    )


def error_429(request, exception=None):
    """429 Too Many Requests page."""
    return render(
        request,
        "public/error_generic.html",
        {
            "error_code": "429",
            "error_title": "Too Many Requests",
            "error_message": "Please wait before trying again.",
        },
        status=429,
    )


def error_500(request):
    """500 Server Error page."""
    return render(
        request,
        "public/error_generic.html",
        {
            "error_code": "500",
            "error_title": "Server Error",
            "error_message": "Something went wrong on our side. Please try again shortly.",
        },
        status=500,
    )
