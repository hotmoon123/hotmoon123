from django.db import models

class Notification(models.Model):
    RECIPIENT_CHOICES = [('landlord', 'Landlord'), ('tenant', 'Tenant')]
    TYPE_CHOICES = [
        ('invoice', 'Invoice'),
        ('maintenance', 'Maintenance'),
        ('lease', 'Lease'),
        ('payment', 'Payment'),
        ('notice', 'Notice'),
        ('inspection', 'Inspection'),
        ('other', 'Other'),
    ]

    recipient_type = models.CharField(max_length=10, choices=RECIPIENT_CHOICES)
    landlord = models.ForeignKey('users.Landlord', on_delete=models.CASCADE, null=True, blank=True, related_name='notifications_sent')
    tenant = models.ForeignKey('users.Tenant', on_delete=models.CASCADE, null=True, blank=True, related_name='notifications_received')
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    title = models.CharField(max_length=255)
    message = models.TextField(default='')
    is_read = models.BooleanField(default=False)
    related_url = models.CharField(max_length=500, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'notifications'
        indexes = [
            models.Index(fields=['is_read']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"{self.title} - {self.recipient_type}"


class ActivityLog(models.Model):
    ACTOR_CHOICES = [('landlord', 'Landlord'), ('tenant', 'Tenant')]
    ACTION_CHOICES = [
        ('login', 'Login'),
        ('logout', 'Logout'),
        ('create', 'Create'),
        ('update', 'Update'),
        ('delete', 'Delete'),
        ('view', 'View'),
        ('download', 'Download'),
        ('upload', 'Upload'),
    ]

    actor_type = models.CharField(max_length=10, choices=ACTOR_CHOICES)
    landlord = models.ForeignKey('users.Landlord', on_delete=models.CASCADE, null=True, blank=True, related_name='activity_logs')
    tenant = models.ForeignKey('users.Tenant', on_delete=models.CASCADE, null=True, blank=True, related_name='activity_logs')
    action = models.CharField(max_length=100, choices=ACTION_CHOICES)
    description = models.TextField(default='')
    related_table = models.CharField(max_length=100, default='')
    related_id = models.BigIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activity_log'
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['action']),
        ]

    def __str__(self):
        return f"{self.actor_type}: {self.action} on {self.related_table}"
