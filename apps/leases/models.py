from django.db import models
from django.conf import settings
from apps.properties.models import Property

class Lease(models.Model):
    """Rental contract between landlord and tenant."""
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('pending', 'Pending Approval'),
        ('terminated', 'Terminated'),
        ('expired', 'Expired'),
    ]

    landlord = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='managed_leases')
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tenancy_leases')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='leases')
    
    start_date = models.DateField()
    end_date = models.DateField()
    rent_amount = models.DecimalField(max_digits=12, decimal_places=2)
    deposit_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    contract_pdf = models.FileField(upload_to='contracts/', null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'leases'

    def __str__(self):
        return f"Lease: {self.tenant.email} at {self.property.unit_number}"
