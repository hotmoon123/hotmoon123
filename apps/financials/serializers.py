"""
Financials App — Serializers

Input validation and output formatting for Financial API.
"""

from rest_framework import serializers
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal
from .models import Invoice, Transaction, Expense, PaymentMethod


class InvoiceSerializer(serializers.ModelSerializer):
    """Serializer for Invoice model."""

    property_address = serializers.CharField(
        source="rental_property.address", read_only=True
    )
    property_unit = serializers.CharField(
        source="rental_property.unit_number", read_only=True
    )
    tenant_name = serializers.SerializerMethodField()
    is_overdue = serializers.ReadOnlyField()

    class Meta:
        model = Invoice
        fields = [
            "id",
            "lease",
            "rental_property",
            "property_address",
            "property_unit",
            "tenant",
            "tenant_name",
            "base_rent",
            "late_fee_amount",
            "total_amount",
            "due_date",
            "status",
            "late_fee_applied",
            "paid_at",
            "is_overdue",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "lease",
            "rental_property",
            "landlord",
            "tenant",
            "base_rent",
            "late_fee_amount",
            "total_amount",
            "late_fee_applied",
            "paid_at",
            "created_at",
        ]

    def get_tenant_name(self, obj):
        if obj.tenant:
            return f"{obj.tenant.first_name} {obj.tenant.last_name}"
        return None


class InvoiceCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating a new invoice."""

    class Meta:
        model = Invoice
        fields = ["lease", "due_date"]

    def validate_lease(self, value):
        """Ensure lease is active."""
        if value.status != "Active":
            raise serializers.ValidationError(
                "Can only create invoices for active leases."
            )
        return value


class TransactionSerializer(serializers.ModelSerializer):
    """Serializer for Transaction model."""

    class Meta:
        model = Transaction
        fields = [
            "id",
            "invoice",
            "amount",
            "gateway_reference",
            "payment_method_last4",
            "created_at",
        ]
        read_only_fields = ["id", "gateway_reference", "created_at"]


class ExpenseSerializer(serializers.ModelSerializer):
    """Serializer for Expense model."""

    property_address = serializers.CharField(
        source="rental_property.address", read_only=True
    )

    class Meta:
        model = Expense
        fields = [
            "id",
            "rental_property",
            "property_address",
            "category",
            "description",
            "amount",
            "expense_date",
            "created_at",
        ]
        read_only_fields = ["id", "landlord", "created_at"]


class ExpenseCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating a new expense."""

    class Meta:
        model = Expense
        fields = [
            "rental_property",
            "category",
            "description",
            "amount",
            "expense_date",
        ]

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")
        return value


class PaymentMethodSerializer(serializers.ModelSerializer):
    """Serializer for PaymentMethod model."""

    is_expired = serializers.ReadOnlyField()
    display_name = serializers.SerializerMethodField()

    class Meta:
        model = PaymentMethod
        fields = [
            "id",
            "last4",
            "card_brand",
            "expiry_month",
            "expiry_year",
            "is_default",
            "is_active",
            "is_expired",
            "display_name",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def get_display_name(self, obj):
        return f"{obj.card_brand} ending in {obj.last4}"


class PaymentSubmitSerializer(serializers.Serializer):
    """Serializer for payment submission."""

    invoice_id = serializers.IntegerField()
    payment_method_id = serializers.IntegerField(required=False)

    def validate_invoice_id(self, value):
        """Validate invoice exists and is outstanding."""
        try:
            invoice = Invoice.objects.get(id=value, status="Outstanding")
        except Invoice.DoesNotExist:
            raise serializers.ValidationError("Invoice not found or already paid.")
        self._invoice = invoice
        return value
