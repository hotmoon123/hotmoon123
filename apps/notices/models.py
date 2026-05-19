from django.db import models

class Notice(models.Model):
    landlord = models.ForeignKey('users.Landlord', on_delete=models.CASCADE, related_name='notices')

    title = models.CharField(max_length=255)
    body = models.TextField()
    is_pinned = models.BooleanField(default=False)
    expires_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'notices'
        indexes = [
            models.Index(fields=['is_pinned']),
            models.Index(fields=['expires_at']),
        ]

    def __str__(self):
        return f"{self.title}"
