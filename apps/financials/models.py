from django.db import models
from django.conf import settings
from apps.leases.models import Lease

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

    landlord = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='issued_invoices')
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_invoices')
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE, related_name='invoices')
    
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    due_date = models.DateField()
    
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
