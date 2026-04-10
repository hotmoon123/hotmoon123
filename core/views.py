from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def render_placeholder(request, page_title, page_description, portal="landlord"):
    """Render a reusable in-progress page shell for unfinished routes."""
    return render(
        request,
        "shared/coming_soon.html",
        {
            "page_title": page_title,
            "page_description": page_description,
            "portal": portal,
        },
    )


def index_view(request):
    """Home page - redirect to login or dashboard based on auth."""
    from django.shortcuts import redirect

    return redirect("login_page")


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
    return render_placeholder(
        request,
        "Verify Email",
        "Email verification flow page is being finalized.",
        portal="public",
    )


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
    return render_placeholder(
        request,
        "Financials",
        "Invoice ledger, exports, and payment analytics are in progress.",
        portal="landlord",
    )


def landlord_tenants(request):
    """Tenant directory page."""
    return render_placeholder(
        request,
        "Tenant Directory",
        "Tenant CRM drawer and filters are in progress.",
        portal="landlord",
    )


def landlord_maintenance(request):
    """Maintenance kanban board."""
    return render_placeholder(
        request,
        "Maintenance",
        "Kanban workflow and ticket actions are in progress.",
        portal="landlord",
    )


def landlord_chat(request):
    """Real-time chat page."""
    return render_placeholder(
        request,
        "Chat",
        "Real-time landlord chat interface is in progress.",
        portal="landlord",
    )


def landlord_documents(request):
    """Document management page."""
    return render_placeholder(
        request,
        "Documents",
        "Vault upload and secure document actions are in progress.",
        portal="landlord",
    )


def landlord_analytics(request):
    """Analytics and reporting page."""
    return render_placeholder(
        request,
        "Analytics",
        "Charts and reporting dashboards are in progress.",
        portal="landlord",
    )


def landlord_notifications(request):
    """Notification center page."""
    return render_placeholder(
        request,
        "Notifications",
        "Notification feed and read states are in progress.",
        portal="landlord",
    )


def landlord_settings(request):
    """Settings and profile page."""
    return render_placeholder(
        request,
        "Settings",
        "Profile, security, and preference settings are in progress.",
        portal="landlord",
    )


def landlord_automations(request):
    """Automation control panel page."""
    return render_placeholder(
        request,
        "Automations",
        "Cron toggle controls and automation status are in progress.",
        portal="landlord",
    )


def landlord_buildings(request):
    """Multi-unit building management page."""
    return render_placeholder(
        request,
        "Buildings",
        "Multi-unit hierarchy and bulk actions are in progress.",
        portal="landlord",
    )


def landlord_expenses(request):
    """Expense and ROI ledger page."""
    return render_placeholder(
        request,
        "Expenses",
        "Expense logging and ROI ledger are in progress.",
        portal="landlord",
    )


# ─── Tenant Pages ─────────────────────────────────────────────


def tenant_dashboard(request):
    """Tenant dashboard with balance overview."""
    return render(request, "tenant/dashboard.html")


def tenant_payments(request):
    """Rent payment page."""
    return render_placeholder(
        request,
        "Payments",
        "Invoice history and payment flow are in progress.",
        portal="tenant",
    )


def tenant_lease(request):
    """Lease details page."""
    return render_placeholder(
        request,
        "My Lease",
        "Lease details and document access are in progress.",
        portal="tenant",
    )


def tenant_maintenance(request):
    """Maintenance ticket submission page."""
    return render_placeholder(
        request,
        "Maintenance",
        "Ticket submission and status tracking are in progress.",
        portal="tenant",
    )


def tenant_chat(request):
    """Chat with landlord page."""
    return render_placeholder(
        request,
        "Chat",
        "Tenant real-time chat interface is in progress.",
        portal="tenant",
    )


def tenant_inspection(request):
    """Move-in/move-out inspection page."""
    return render_placeholder(
        request,
        "Inspection",
        "Move-in and move-out checklist flow is in progress.",
        portal="tenant",
    )


def tenant_payment_methods(request):
    """Payment methods management page."""
    return render_placeholder(
        request,
        "Payment Methods",
        "Saved cards and auto-pay setup are in progress.",
        portal="tenant",
    )


def tenant_notice_board(request):
    """Landlord notice board page."""
    return render_placeholder(
        request,
        "Notice Board",
        "Tenant announcements feed is in progress.",
        portal="tenant",
    )


def tenant_compliance(request):
    """Compliance documents page."""
    return render_placeholder(
        request,
        "Compliance",
        "Compliance uploads and verification statuses are in progress.",
        portal="tenant",
    )


def tenant_profile(request):
    """Profile settings page."""
    return render_placeholder(
        request,
        "Profile",
        "Tenant profile and notifications settings are in progress.",
        portal="tenant",
    )


def tenant_history(request):
    """Payment history page."""
    return render_placeholder(
        request,
        "History",
        "Chronological tenant activity and receipts are in progress.",
        portal="tenant",
    )


# ─── Public Pages ─────────────────────────────────────────────


def payment_success(request):
    """Payment success page."""
    return render_placeholder(
        request,
        "Payment Success",
        "Final payment confirmation screen is in progress.",
        portal="public",
    )


def payment_cancelled(request):
    """Payment cancelled page."""
    return render_placeholder(
        request,
        "Payment Cancelled",
        "Payment retry guidance screen is in progress.",
        portal="public",
    )


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
