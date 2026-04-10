"""
Properties App — Database Models (Layer 9)

Models align with database schema in docs/documents file.md:
- buildings: Parent groups for multi-unit properties
- properties: Individual rental units with address, rent, and status
"""

from django.db import models
from django.conf import settings


class Building(models.Model):
    """
    Parent grouping for multi-unit properties.
    Example: "Sunset Apartments" contains units 101, 102, 103.
    """

    landlord = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="buildings",
        db_column="landlord_id",
    )
    name = models.CharField(max_length=255)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)

    class Meta:
        db_table = "buildings"
        indexes = [
            models.Index(fields=["landlord"], name="idx_buildings_landlord"),
        ]

    def __str__(self):
        return f"{self.name} ({self.landlord})"


class Property(models.Model):
    """
    Individual rental unit.
    Can belong to a Building (for multi-unit) or stand alone.
    """

    STATUS_CHOICES = [
        ("Vacant", "Vacant"),
        ("Leased", "Leased"),
    ]

    landlord = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="properties",
        db_column="landlord_id",
    )
    building = models.ForeignKey(
        Building,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="properties",
        db_column="building_id",
    )
    unit_number = models.CharField(max_length=50)
    address = models.TextField()
    base_rent = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Vacant")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)

    class Meta:
        db_table = "properties"
        indexes = [
            models.Index(fields=["landlord"], name="idx_properties_landlord"),
            models.Index(fields=["status"], name="idx_properties_status"),
            models.Index(fields=["building"], name="idx_properties_building"),
        ]

    def __str__(self):
        return f"Unit {self.unit_number} - {self.address}"

    @property
    def is_vacant(self):
        return self.status == "Vacant"

    @property
    def is_leased(self):
        return self.status == "Leased"
