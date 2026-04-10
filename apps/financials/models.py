"""
Financials App — Database Models (Layer 9)

Models align with database schema in docs/documents file.md:
- invoices: Monthly rent invoices generated for tenants
- transactions: Record of all payments (append-only)
- expenses: Property expenses for ROI calculation
- payment_methods: Tenant stored payment methods
"""

from django.db import models
from django.conf import settings


class Invoice(models.Model):
    """
    Monthly rent invoice generated for a tenant.
    Tracks payment status and late fee application.
    """

    STATUS_CHOICES = [
        ("Outstanding", "Outstanding"),
        ("Paid", "Paid"),
        ("Cancelled", "Cancelled"),
    ]

    lease = models.ForeignKey(
        "leases.Lease",
        on_delete=models.CASCADE,
        related_name="invoices",
        db_column="lease_id",
    )
    tenant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tenant_invoices",
        db_column="tenant_id",
    )
    rental_property = models.ForeignKey(
        "properties.Property",
        on_delete=models.CASCADE,
        related_name="invoices",
        db_column="property_id",
    )
    landlord = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="landlord_invoices",
        db_column="landlord_id",
    )
    base_rent = models.DecimalField(max_digits=10, decimal_places=2)
    late_fee_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="Outstanding"
    )
    late_fee_applied = models.BooleanField(default=False)
    paid_at = models.DateTimeField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "invoices"
        indexes = [
            models.Index(fields=["tenant"], name="idx_invoices_tenant"),
            models.Index(fields=["landlord"], name="idx_invoices_landlord"),
            models.Index(fields=["status"], name="idx_invoices_status"),
            models.Index(fields=["due_date"], name="idx_invoices_due_date"),
            models.Index(fields=["lease"], name="idx_invoices_lease"),
        ]

    def __str__(self):
        return f"Invoice #{self.id} - {self.total_amount} (Due: {self.due_date})"

    @property
    def is_overdue(self):
        from datetime import date

        return self.status == "Outstanding" and self.due_date < date.today()

    @property
    def is_paid(self):
        return self.status == "Paid"


class Transaction(models.Model):
    """
    Record of all payments (append-only — no updates or deletes).
    Contains payment gateway reference for audit trail.
    """

    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE,
        related_name="transactions",
        db_column="invoice_id",
    )
    tenant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tenant_transactions",
        db_column="tenant_id",
    )
    landlord = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="landlord_transactions",
        db_column="landlord_id",
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    gateway_reference = models.CharField(max_length=255, unique=True)
    payment_method_last4 = models.CharField(max_length=4, blank=True, default="")
    idempotency_key = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "transactions"
        indexes = [
            models.Index(fields=["invoice"], name="idx_transactions_invoice"),
            models.Index(fields=["tenant"], name="idx_transactions_tenant"),
        ]

    def __str__(self):
        return f"Transaction #{self.id} - {self.amount}"


class Expense(models.Model):
    """
    Property expense record for ROI calculation.
    Examples: repairs, taxes, maintenance costs.
    """

    CATEGORY_CHOICES = [
        ("repairs", "Repairs"),
        ("maintenance", "Maintenance"),
        ("taxes", "Taxes"),
        ("insurance", "Insurance"),
        ("utilities", "Utilities"),
        ("management", "Management"),
        ("other", "Other"),
    ]

    rental_property = models.ForeignKey(
        "properties.Property",
        on_delete=models.CASCADE,
        related_name="expenses",
        db_column="property_id",
    )
    landlord = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="expenses",
        db_column="landlord_id",
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "expenses"
        indexes = [
            models.Index(fields=["rental_property"], name="idx_expenses_property"),
            models.Index(fields=["landlord"], name="idx_expenses_landlord"),
            models.Index(fields=["category"], name="idx_expenses_category"),
            models.Index(fields=["expense_date"], name="idx_expenses_date"),
        ]

    def __str__(self):
        return f"{self.category} - {self.amount} ({self.expense_date})"


class PaymentMethod(models.Model):
    """
    Stored payment methods for tenants (auto-pay).
    Card details stored as tokenized references from payment gateway.
    """

    tenant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="payment_methods",
        db_column="tenant_id",
    )
    gateway_token = models.CharField(max_length=255)
    last4 = models.CharField(max_length=4)
    card_brand = models.CharField(max_length=20)
    expiry_month = models.IntegerField()
    expiry_year = models.IntegerField()
    is_default = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "payment_methods"
        indexes = [
            models.Index(fields=["tenant"], name="idx_payment_methods_tenant"),
        ]

    def __str__(self):
        return f"{self.card_brand} ****{self.last4}"

    @property
    def is_expired(self):
        from datetime import date

        now = date.today()
        return self.expiry_year < now.year or (
            self.expiry_year == now.year and self.expiry_month < now.month
        )
