from django.db import models

class AutomationRule(models.Model):
    TRIGGER_CHOICES = [
        ('invoice_due', 'Invoice Due'),
        ('lease_expiry', 'Lease Expiry'),
        ('payment_received', 'Payment Received'),
        ('maintenance_request', 'Maintenance Request'),
        ('document_upload', 'Document Upload'),
    ]
    ACTION_CHOICES = [
        ('send_notification', 'Send Notification'),
        ('send_email', 'Send Email'),
        ('create_invoice', 'Create Invoice'),
        ('update_status', 'Update Status'),
        ('generate_report', 'Generate Report'),
    ]

    landlord = models.ForeignKey('users.Landlord', on_delete=models.CASCADE, related_name='automation_rules')
    name = models.CharField(max_length=255)
    trigger_event = models.CharField(max_length=100, choices=TRIGGER_CHOICES)
    action = models.CharField(max_length=100, choices=ACTION_CHOICES)
    conditions = models.TextField(default='')
    is_active = models.BooleanField(default=True)
    last_run_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'automation_rules'
        indexes = [
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return f"{self.name} - {self.trigger_event}"
