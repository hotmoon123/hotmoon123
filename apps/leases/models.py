"""
Leases App — Database Models (Layer 9)

Models align with database schema in docs/documents file.md:
- leases: Rental agreements between landlord and tenant
- invitations: Email invitations for tenants to join via lease
"""

from django.db import models
from django.conf import settings


class Lease(models.Model):
    """
    Rental agreement linking a property to a tenant.
    Contains lease terms: start date, end date, monthly rent.
    """

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Active", "Active"),
        ("Expired", "Expired"),
        ("Terminated", "Terminated"),
    ]

    rental_property = models.ForeignKey(
        "properties.Property",
        on_delete=models.CASCADE,
        related_name="leases",
        db_column="property_id",
    )
    landlord = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="leases_as_landlord",
        db_column="landlord_id",
    )
    tenant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="leases_as_tenant",
        db_column="tenant_id",
    )
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    signed_at = models.DateTimeField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)

    class Meta:
        db_table = "leases"
        indexes = [
            models.Index(fields=["rental_property"], name="idx_leases_property"),
            models.Index(fields=["landlord"], name="idx_leases_landlord"),
            models.Index(fields=["tenant"], name="idx_leases_tenant"),
            models.Index(fields=["status"], name="idx_leases_status"),
            models.Index(fields=["start_date", "end_date"], name="idx_leases_dates"),
        ]

    def __str__(self):
        return (
            f"Lease for {self.rental_property} ({self.start_date} to {self.end_date})"
        )

    @property
    def is_active(self):
        return self.status == "Active"

    @property
    def is_pending(self):
        return self.status == "Pending"

    @property
    def is_expired(self):
        return self.status == "Expired"

    @property
    def days_until_expiry(self):
        from datetime import date

        return (self.end_date - date.today()).days


class Invitation(models.Model):
    """
    Email invitation for a tenant to join a lease.
    Contains encrypted token for secure invitation link.
    """

    lease = models.ForeignKey(
        Lease,
        on_delete=models.CASCADE,
        related_name="invitations",
        db_column="lease_id",
    )
    landlord = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_invitations",
        db_column="landlord_id",
    )
    email = models.EmailField()
    token_hash = models.CharField(max_length=255, unique=True)
    expires_at = models.DateTimeField()
    accepted_at = models.DateTimeField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "invitations"
        indexes = [
            models.Index(fields=["token_hash"], name="idx_invitations_token"),
            models.Index(fields=["lease"], name="idx_invitations_lease"),
        ]

    def __str__(self):
        return f"Invitation for {self.email} to lease {self.lease_id}"

    @property
    def is_expired(self):
        from django.utils import timezone

        return timezone.now() > self.expires_at

    @property
    def is_accepted(self):
        return self.accepted_at is not None
