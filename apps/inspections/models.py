from django.db import models

class Inspection(models.Model):
    TYPE_CHOICES = [
        ('initial', 'Initial'),
        ('midterm', 'Midterm'),
        ('final', 'Final'),
        ('emergency', 'Emergency'),
    ]
    CONDITION_CHOICES = [
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
    ]

    lease = models.ForeignKey('leases.Lease', on_delete=models.CASCADE, related_name='inspections')
    landlord = models.ForeignKey('users.Landlord', on_delete=models.CASCADE, related_name='inspections_conducted')
    tenant = models.ForeignKey('users.Tenant', on_delete=models.CASCADE, related_name='inspections_participated')
    property = models.ForeignKey('properties.Property', on_delete=models.CASCADE, related_name='inspections')

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='good')
    notes = models.TextField(default='')
    photos = models.TextField(default='')
    conducted_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'inspections'
        indexes = [
            models.Index(fields=['lease_id']),
        ]

    def __str__(self):
        return f"Inspection {self.type} - Lease {self.lease.id}"
