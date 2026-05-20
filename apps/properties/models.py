from django.db import models
from apps.users.models import Landlord


class Building(models.Model):
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, related_name='buildings')
    name = models.CharField(max_length=255)
    address = models.TextField()
    description = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'buildings'

    def __str__(self):
        return f"{self.name} ({self.landlord.email})"


class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('duplex', 'Duplex'),
        ('bungalow', 'Bungalow'),
        ('commercial', 'Commercial'),
        ('other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('maintenance', 'Under Maintenance'),
        ('unavailable', 'Unavailable'),
    ]

    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, related_name='properties')
    building = models.ForeignKey(Building, on_delete=models.SET_NULL, null=True, blank=True, related_name='properties')
    unit_number = models.CharField(max_length=50)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES, default='apartment')
    address = models.TextField()
    city = models.CharField(max_length=100)
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    square_feet = models.IntegerField(default=0)
    monthly_rent = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, default='')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'properties'
        unique_together = ('landlord', 'unit_number')

    def __str__(self):
        return f"{self.unit_number} - {self.address}"
