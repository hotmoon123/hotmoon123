from django.db import models
from apps.users.models import Landlord, Tenant
from apps.properties.models import Property


class MaintenanceTicket(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('emergency', 'Emergency'),
    ]
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('pending_parts', 'Pending Parts'),
        ('done', 'Completed'),
    ]

    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, related_name='received_tickets')
    tenant = models.ForeignKey(Tenant, on_delete=models.SET_NULL, null=True, blank=True, related_name='submitted_tickets')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='tickets')
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    photo = models.ImageField(upload_to='maintenance/', null=True, blank=True)
    estimated_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'maintenance_tickets'

    def __str__(self):
        return f"Ticket #{self.id}: {self.title}"
