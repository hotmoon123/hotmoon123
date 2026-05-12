"""
Financials App — API Views (Layer 5)

RESTful CRUD operations for Invoices, Transactions, Expenses, PaymentMethods.
"""

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, Count, Q
from django.db.models.functions import TruncMonth
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal

from .models import Invoice, Transaction, Expense, PaymentMethod
from .serializers import (
    InvoiceSerializer,
    InvoiceCreateSerializer,
    TransactionSerializer,
    ExpenseSerializer,
    ExpenseCreateSerializer,
    PaymentMethodSerializer,
    PaymentSubmitSerializer,
)


class InvoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoints for managing invoices.
    """

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "landlord":
            return Invoice.objects.filter(landlord=user).select_related(
                "rental_property", "tenant", "lease"
            )
        else:
            return Invoice.objects.filter(tenant=user).select_related(
                "rental_property", "landlord", "lease"
            )

    def get_serializer_class(self):
        if self.action == "create":
            return InvoiceCreateSerializer
        return InvoiceSerializer

    def perform_create(self, serializer):
        """Set landlord from lease on create."""
        lease = serializer.validated_data["lease"]
        invoice = serializer.save(
            landlord=lease.landlord, rental_property=lease.property
        )

    @action(detail=False, methods=["get"])
    def outstanding(self, request):
        """GET /api/v1/financials/invoices/outstanding/ - Get overdue invoices."""
        today = timezone.now().date()
        invoices = (
            self.get_queryset()
            .filter(status="Outstanding", due_date__lt=today)
            .order_by("due_date")
        )
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def summary(self, request):
        """GET /api/v1/financials/invoices/summary/ - Dashboard summary."""
        user = request.user
        queryset = self.get_queryset()

        total_outstanding = queryset.filter(status="Outstanding").aggregate(
            total=Sum("total_amount")
        )["total"] or Decimal("0.00")

        overdue_count = queryset.filter(
            status="Outstanding", due_date__lt=timezone.now().date()
        ).count()

        paid_this_month = queryset.filter(
            status="Paid",
            paid_at__gte=timezone.now().replace(
                day=1, hour=0, minute=0, second=0, microsecond=0
            ),
        ).aggregate(total=Sum("total_amount"))["total"] or Decimal("0.00")

        return Response(
            {
                "total_outstanding": float(total_outstanding),
                "overdue_count": overdue_count,
                "paid_this_month": float(paid_this_month),
            }
        )


class TransactionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoints for viewing transactions.
    """

    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "landlord":
            return Transaction.objects.filter(landlord=user)
        return Transaction.objects.filter(tenant=user)


class ExpenseViewSet(viewsets.ModelViewSet):
    """
    API endpoints for managing expenses.
    """

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(landlord=self.request.user).select_related(
            "rental_property"
        )

    def get_serializer_class(self):
        if self.action == "create":
            return ExpenseCreateSerializer
        return ExpenseSerializer

    def perform_create(self, serializer):
        serializer.save(landlord=self.request.user)

    @action(detail=False, methods=["get"])
    def summary(self, request):
        """GET /api/v1/financials/expenses/summary/ - ROI summary by property."""
        expenses = self.get_queryset()

        by_property = (
            expenses.values("rental_property__id", "rental_property__address")
            .annotate(total=Sum("amount"))
            .order_by("-total")
        )

        by_category = (
            expenses.values("category").annotate(total=Sum("amount")).order_by("-total")
        )

        total_this_month = expenses.filter(
            expense_date__gte=timezone.now().replace(day=1)
        ).aggregate(total=Sum("amount"))["total"] or Decimal("0.00")

        return Response(
            {
                "by_property": list(by_property),
                "by_category": list(by_category),
                "total_this_month": float(total_this_month),
            }
        )


class PaymentMethodViewSet(viewsets.ModelViewSet):
    """
    API endpoints for managing tenant payment methods.
    """

    serializer_class = PaymentMethodSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PaymentMethod.objects.filter(tenant=self.request.user, is_active=True)

    def perform_create(self, serializer):
        payment_method = serializer.save(tenant=self.request.user)
        if payment_method.is_default:
            PaymentMethod.objects.filter(tenant=self.request.user).exclude(
                pk=payment_method.pk
            ).update(is_default=False)

    @action(detail=True, methods=["post"])
    def set_default(self, request, pk=None):
        """POST /api/v1/financials/payment-methods/{id}/set_default/"""
        payment_method = self.get_object()
        PaymentMethod.objects.filter(tenant=request.user).update(is_default=False)
        payment_method.is_default = True
        payment_method.save()
        return Response(PaymentMethodSerializer(payment_method).data)

    @action(detail=False, methods=["post"])
    def pay(self, request):
        """
        POST /api/v1/financials/payment-methods/pay/

        Process a rent payment. In production, this would integrate with
        Stripe/Paystack payment gateway.
        """
        serializer = PaymentSubmitSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

        invoice = serializer._invoice
        tenant = request.user

        idempotency_key = f"{tenant.id}_{invoice.id}_{timezone.now().date()}"

        if Transaction.objects.filter(idempotency_key=idempotency_key).exists():
            return Response(
                {"errors": {"detail": "This payment has already been processed."}},
                status=status.HTTP_400_BAD_REQUEST,
            )

        import uuid

        gateway_reference = f"txn_{uuid.uuid4().hex[:16]}"

        transaction = Transaction.objects.create(
            invoice=invoice,
            tenant=tenant,
            landlord=invoice.landlord,
            amount=invoice.total_amount,
            gateway_reference=gateway_reference,
            idempotency_key=idempotency_key,
        )

        invoice.status = "Paid"
        invoice.paid_at = timezone.now()
        invoice.save()

        return Response(
            {
                "message": "Payment successful",
                "transaction": TransactionSerializer(transaction).data,
                "receipt_id": gateway_reference,
            }
        )
