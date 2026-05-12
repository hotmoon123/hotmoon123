from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, Q, Avg
from django.utils import timezone
from decimal import Decimal
from apps.properties.models import Property
from apps.leases.models import Lease
from apps.financials.models import Invoice, Transaction
from apps.maintenance.models import MaintenanceTicket


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
    # Ensure user is authenticated and is a landlord
    if not request.user.is_authenticated:
        return redirect('login_page')
    
    if request.user.role != 'landlord':
        return redirect('tenant_dashboard')
    
    user = request.user
    
    # Fetch real metrics from database
    properties = Property.objects.filter(landlord=user)
    total_properties = properties.count()
    occupied_properties = properties.filter(status='occupied').count()
    occupancy_rate = (occupied_properties / total_properties * 100) if total_properties > 0 else 0
    
    # Monthly revenue from paid invoices
    current_month = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    monthly_revenue = Invoice.objects.filter(
        landlord=user,
        status='paid',
        paid_at__gte=current_month
    ).aggregate(total=Sum('amount_paid'))['total'] or Decimal('0.00')
    
    # Open maintenance tickets
    open_tickets = MaintenanceTicket.objects.filter(
        landlord=user,
        status__in=['todo', 'in_progress', 'pending_parts']
    ).count()
    
    # Expiring leases (next 60 days)
    sixty_days_from_now = timezone.now().date() + timezone.timedelta(days=60)
    expiring_leases = Lease.objects.filter(
        landlord=user,
        status='active',
        end_date__lte=sixty_days_from_now,
        end_date__gte=timezone.now().date()
    ).select_related('tenant', 'property')[:5]
    
    # Recent transactions
    recent_transactions = Transaction.objects.filter(
        landlord=user
    ).select_related('invoice', 'tenant').order_by('-created_at')[:10]
    
    context = {
        'total_properties': total_properties,
        'occupied_properties': occupied_properties,
        'occupancy_rate': round(occupancy_rate, 1),
        'monthly_revenue': monthly_revenue,
        'open_tickets': open_tickets,
        'expiring_leases': expiring_leases,
        'recent_transactions': recent_transactions,
    }
    
    return render(request, "landlord/dashboard.html", context)


def landlord_properties(request):
    """Property portfolio management."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.user.role != 'landlord':
        return redirect('tenant_dashboard')
    return render(request, "landlord/properties.html")


def landlord_leases(request):
    """Lease management page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.user.role != 'landlord':
        return redirect('tenant_dashboard')
    return render(request, "landlord/leases.html")


def landlord_financials(request):
    """Financial management page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.user.role != 'landlord':
        return redirect('tenant_dashboard')
    return render(request, "landlord/financials.html")


def landlord_tenants(request):
    """Tenant directory page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.user.role != 'landlord':
        return redirect('tenant_dashboard')
    return render(request, "landlord/tenants.html")


def landlord_maintenance(request):
    """Maintenance kanban board."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.user.role != 'landlord':
        return redirect('tenant_dashboard')
    return render(request, "landlord/maintenance.html")


def landlord_chat(request):
    """Real-time chat page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.user.role != 'landlord':
        return redirect('tenant_dashboard')
    return render(request, "landlord/chat.html")


def landlord_documents(request):
    """Document management page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.user.role != 'landlord':
        return redirect('tenant_dashboard')
    return render(request, "landlord/documents.html")


def landlord_analytics(request):
    """Analytics and reporting page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.user.role != 'landlord':
        return redirect('tenant_dashboard')
    return render(request, "landlord/analytics.html")


def landlord_notifications(request):
    """Notification center page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.user.role != 'landlord':
        return redirect('tenant_dashboard')
    return render(request, "landlord/notifications.html")


def landlord_settings(request):
    """Settings and profile page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.user.role != 'landlord':
        return redirect('tenant_dashboard')
    return render(request, "landlord/settings.html")


def landlord_automations(request):
    """Automation control panel page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.user.role != 'landlord':
        return redirect('tenant_dashboard')
    return render(request, "landlord/automations.html")


def landlord_buildings(request):
    """Multi-unit building management page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.user.role != 'landlord':
        return redirect('tenant_dashboard')
    return render(request, "landlord/buildings.html")


def landlord_expenses(request):
    """Expense and ROI ledger page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.user.role != 'landlord':
        return redirect('tenant_dashboard')
    return render(request, "landlord/expenses.html")


# ─── Tenant Pages ─────────────────────────────────────────────


def tenant_dashboard(request):
    """Tenant dashboard with balance overview."""
    # Ensure user is authenticated and is a tenant
    if not request.user.is_authenticated:
        return redirect('login_page')
    
    if request.user.role != 'tenant':
        return redirect('landlord_dashboard')
    
    user = request.user
    
    # Get tenant's active lease
    active_lease = Lease.objects.filter(
        tenant=user,
        status='active'
    ).select_related('property', 'landlord').first()
    
    # Get outstanding invoices
    outstanding_invoices = Invoice.objects.filter(
        tenant=user,
        status__in=['unpaid', 'partial', 'overdue']
    ).order_by('due_date')
    
    # Total balance due
    total_balance = outstanding_invoices.aggregate(
        total=Sum('amount')
    )['total'] or Decimal('0.00')
    
    # Next payment (earliest due date)
    next_payment = outstanding_invoices.first()
    
    # Recent notices/notifications (you can add a Notification model later)
    # For now, using recent invoices as activity
    recent_activity = Invoice.objects.filter(
        tenant=user
    ).order_by('-created_at')[:5]
    
    context = {
        'active_lease': active_lease,
        'outstanding_invoices': outstanding_invoices,
        'total_balance': total_balance,
        'next_payment': next_payment,
        'recent_activity': recent_activity,
    }
    
    return render(request, "tenant/dashboard.html", context)


def tenant_payments(request):
    """Rent payment page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.user.role != 'tenant':
        return redirect('landlord_dashboard')
    return render(request, "tenant/payments.html")


def tenant_lease(request):
    """Lease details page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.user.role != 'tenant':
        return redirect('landlord_dashboard')
    return render(request, "tenant/lease.html")


def tenant_maintenance(request):
    """Maintenance ticket submission page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.user.role != 'tenant':
        return redirect('landlord_dashboard')
    return render(request, "tenant/maintenance.html")


def tenant_chat(request):
    """Chat with landlord page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.user.role != 'tenant':
        return redirect('landlord_dashboard')
    return render(request, "tenant/chat.html")


def tenant_inspection(request):
    """Move-in/move-out inspection page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.user.role != 'tenant':
        return redirect('landlord_dashboard')
    return render(request, "tenant/inspection.html")


def tenant_payment_methods(request):
    """Payment methods management page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.user.role != 'tenant':
        return redirect('landlord_dashboard')
    return render(request, "tenant/payment_methods.html")


def tenant_notice_board(request):
    """Landlord notice board page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.user.role != 'tenant':
        return redirect('landlord_dashboard')
    return render(request, "tenant/notice_board.html")


def tenant_compliance(request):
    """Compliance documents page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.user.role != 'tenant':
        return redirect('landlord_dashboard')
    return render(request, "tenant/compliance.html")


def tenant_profile(request):
    """Profile settings page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.user.role != 'tenant':
        return redirect('landlord_dashboard')
    return render(request, "tenant/profile.html")


def tenant_history(request):
    """Payment history page."""
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.user.role != 'tenant':
        return redirect('landlord_dashboard')
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
