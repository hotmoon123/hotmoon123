import secrets
from django.db import models
from apps.users.models import Landlord, Tenant
from apps.properties.models import Property


class Lease(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Approval'),
        ('active', 'Active'),
        ('terminated', 'Terminated'),
        ('expired', 'Expired'),
    ]

    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, related_name='managed_leases')
    tenant = models.ForeignKey(Tenant, on_delete=models.SET_NULL, null=True, blank=True, related_name='tenancy_leases')
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
        tenant_name = self.tenant.email if self.tenant else 'Pending'
        return f"Lease: {tenant_name} @ {self.property.unit_number}"


class Invitation(models.Model):
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE, related_name='invitations')
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, related_name='sent_invitations')
    email = models.EmailField()
    token_hash = models.CharField(max_length=255, unique=True)
    expires_at = models.DateTimeField()
    accepted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'invitations'

    @property
    def is_expired(self):
        from django.utils import timezone
        return timezone.now() > self.expires_at

    def __str__(self):
        return f"Invitation for {self.email} to lease {self.lease.id}"
