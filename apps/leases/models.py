from django.db import models
from apps.properties.models import Property

class Lease(models.Model):
    """Rental contract between landlord and tenant."""
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('pending', 'Pending Approval'),
        ('terminated', 'Terminated'),
        ('expired', 'Expired'),
    ]

    landlord = models.ForeignKey('users.Landlord', on_delete=models.CASCADE, related_name='managed_leases')
    tenant = models.ForeignKey('users.Tenant', on_delete=models.SET_NULL, null=True, blank=True, related_name='tenancy_leases')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='leases')
    
    start_date = models.DateField()
    end_date = models.DateField()
    rent_amount = models.DecimalField(max_digits=12, decimal_places=2)
    deposit_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    contract_pdf = models.FileField(upload_to='contracts/', null=True, blank=True)
    signed_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'leases'

    def __str__(self):
        return f"Lease: {self.tenant.email if self.tenant else 'Pending'} at {self.property.unit_number}"


class Invitation(models.Model):
    """Tenant invitation to join a lease."""
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE, related_name='invitations')
    landlord = models.ForeignKey('users.Landlord', on_delete=models.CASCADE, related_name='sent_invitations')
    email = models.EmailField()
    token_hash = models.CharField(max_length=255)
    expires_at = models.DateTimeField()
    accepted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'invitations'

    def __str__(self):
        return f"Invitation for {self.email} to lease {self.lease.id}"

    @property
    def is_expired(self):
        """Check if invitation has expired."""
        from django.utils import timezone
        return timezone.now() > self.expires_at
