from django.db import models
from apps.leases.models import Lease
from apps.properties.models import Property

class Invoice(models.Model):
    """Monthly billing for a lease."""
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

    landlord = models.ForeignKey('users.Landlord', on_delete=models.CASCADE, related_name='issued_invoices')
    tenant = models.ForeignKey('users.Tenant', on_delete=models.CASCADE, related_name='received_invoices')
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

    def __str__(self):
        return f"Invoice {self.id}: {self.tenant.email} - {self.status}"
    
    @property
    def balance_due(self):
        return self.amount - self.amount_paid


class Transaction(models.Model):
    """Payment transaction record."""
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='transactions')
    tenant = models.ForeignKey('users.Tenant', on_delete=models.CASCADE, related_name='payment_transactions')
    landlord = models.ForeignKey('users.Landlord', on_delete=models.CASCADE, related_name='received_transactions')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    gateway_reference = models.CharField(max_length=255, blank=True, default='')
    idempotency_key = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'transactions'

    def __str__(self):
        return f"Transaction {self.gateway_reference}: {self.amount}"


class Expense(models.Model):
    """Property expense tracking."""
    CATEGORY_CHOICES = [
        ('maintenance', 'Maintenance'),
        ('repair', 'Repair'),
        ('utility', 'Utility'),
        ('tax', 'Tax'),
        ('insurance', 'Insurance'),
        ('other', 'Other'),
    ]

    landlord = models.ForeignKey('users.Landlord', on_delete=models.CASCADE, related_name='expenses')
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
        return f"Expense: {self.category} - {self.amount}"


class PaymentMethod(models.Model):
    """Tenant payment methods (cards, etc.)."""
    TYPE_CHOICES = [
        ('card', 'Credit/Debit Card'),
        ('bank', 'Bank Account'),
        ('mobile', 'Mobile Money'),
    ]

    tenant = models.ForeignKey('users.Tenant', on_delete=models.CASCADE, related_name='payment_methods')
    method_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='card')
    provider = models.CharField(max_length=100, default='stripe')  # stripe, paystack, etc.
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
        return f"{self.tenant.email} - {self.method_type} ending in {self.last_four}"
