from django.db import models
from apps.users.models import Landlord, Tenant
from apps.leases.models import Lease
from apps.properties.models import Property


class Invoice(models.Model):
    TYPE_CHOICES = [
        ('rent', 'Rent'),
        ('utility', 'Utility'),
        ('penalty', 'Penalty'),
        ('deposit', 'Deposit'),
    ]
    STATUS_CHOICES = [
        ('unpaid', 'Unpaid'),
        ('partial', 'Partially Paid'),
        ('paid', 'Fully Paid'),
        ('overdue', 'Overdue'),
    ]

    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, related_name='issued_invoices')
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='received_invoices')
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE, related_name='invoices')
    rental_property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='invoices', null=True, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    due_date = models.DateField()
    paid_at = models.DateTimeField(null=True, blank=True)
    invoice_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='rent')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='unpaid')
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'invoices'

    @property
    def balance_due(self):
        return self.amount - self.amount_paid

    def __str__(self):
        return f"Invoice {self.id}: {self.tenant.email} - {self.status}"


class Transaction(models.Model):
    MOMO_PROVIDER_CHOICES = [
        ('mtn', 'MTN Mobile Money'),
        ('vodafone', 'Vodafone Cash'),
        ('telecel', 'Telecel Cash'),
        ('bank', 'Bank Transfer'),
    ]

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='transactions')
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='payment_transactions')
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, related_name='received_transactions')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    momo_provider = models.CharField(max_length=20, choices=MOMO_PROVIDER_CHOICES, null=True, blank=True)
    momo_number = models.CharField(max_length=30, blank=True)
    transaction_reference = models.CharField(max_length=255, blank=True, unique=True)
    gateway_reference = models.CharField(max_length=255, blank=True, default='')
    idempotency_key = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'transactions'

    def __str__(self):
        return f"Transaction {self.transaction_reference}: {self.amount} GHS"


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('maintenance', 'Maintenance'),
        ('repair', 'Repair'),
        ('utility', 'Utility'),
        ('tax', 'Tax'),
        ('insurance', 'Insurance'),
        ('other', 'Other'),
    ]

    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, related_name='expenses')
    rental_property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='expenses', null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    expense_date = models.DateField()
    receipt = models.FileField(upload_to='expense_receipts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'expenses'

    def __str__(self):
        return f"Expense: {self.category} - {self.amount} GHS"


class PaymentMethod(models.Model):
    METHOD_TYPE_CHOICES = [
        ('mtn', 'MTN Mobile Money'),
        ('vodafone', 'Vodafone Cash'),
        ('telecel', 'Telecel Cash'),
        ('bank', 'Bank Account'),
        ('card', 'Credit/Debit Card'),
    ]

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='payment_methods')
    method_type = models.CharField(max_length=20, choices=METHOD_TYPE_CHOICES, default='mtn')
    provider = models.CharField(max_length=100, default='mtn')
    momo_number = models.CharField(max_length=30, blank=True)
    last_four = models.CharField(max_length=4, default='0000')
    exp_month = models.IntegerField(null=True, blank=True)
    exp_year = models.IntegerField(null=True, blank=True)
    is_default = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    gateway_customer_id = models.CharField(max_length=255, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'payment_methods'

    def __str__(self):
        return f"{self.tenant.email} - {self.get_method_type_display()}"
