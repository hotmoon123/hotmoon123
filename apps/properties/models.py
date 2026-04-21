from django.db import models
from django.conf import settings

class Building(models.Model):
    """Parent group for properties (e.g., 'Sunset Apartments')."""
    landlord = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='buildings')
    name = models.CharField(max_length=255)
    address = models.TextField()
    description = models.TextField(blank=True, null=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'buildings'

    def __str__(self):
        return self.name

class Property(models.Model):
    """Individual rental units."""
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('maintenance', 'Under Maintenance'),
    ]
    TYPE_CHOICES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('office', 'Office'),
        ('studio', 'Studio'),
    ]

    landlord = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='properties')
    building = models.ForeignKey(Building, on_delete=models.SET_NULL, null=True, blank=True, related_name='units')
    unit_number = models.CharField(max_length=50)
    property_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='apartment')
    rent_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    description = models.TextField(blank=True, null=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'properties'
        verbose_name_plural = 'properties'

    def __str__(self):
        return f"{self.unit_number} - {self.building.name if self.building else 'Standalone'}"
