from django.db import models

class Message(models.Model):
    SENDER_CHOICES = [('landlord', 'Landlord'), ('tenant', 'Tenant')]

    landlord = models.ForeignKey('users.Landlord', on_delete=models.CASCADE, related_name='sent_messages')
    tenant = models.ForeignKey('users.Tenant', on_delete=models.CASCADE, related_name='received_messages')
    sender_type = models.CharField(max_length=10, choices=SENDER_CHOICES)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'messages'
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['is_read']),
        ]

    def __str__(self):
        return f"Message from {self.sender_type} at {self.created_at}"
