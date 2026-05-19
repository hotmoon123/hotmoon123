from django.db import models

class Document(models.Model):
    landlord = models.ForeignKey('users.Landlord', on_delete=models.CASCADE, related_name='documents')
    tenant = models.ForeignKey('users.Tenant', on_delete=models.SET_NULL, null=True, blank=True, related_name='documents')
    lease = models.ForeignKey('leases.Lease', on_delete=models.SET_NULL, null=True, blank=True, related_name='documents')
    property = models.ForeignKey('properties.Property', on_delete=models.SET_NULL, null=True, blank=True, related_name='documents')

    title = models.CharField(max_length=255)
    file_path = models.CharField(max_length=500)
    file_type = models.CharField(max_length=50, default='')
    file_size = models.PositiveIntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'documents'
        indexes = [
            models.Index(fields=['lease_id']),
        ]

    def __str__(self):
        return f"{self.title} - {self.file_type}"


class ComplianceDocument(models.Model):
    landlord = models.ForeignKey('users.Landlord', on_delete=models.CASCADE, related_name='compliance_documents')

    title = models.CharField(max_length=255)
    description = models.TextField(default='')
    file_path = models.CharField(max_length=500)
    category = models.CharField(max_length=100, default='')
    is_mandatory = models.BooleanField(default=False)
    valid_until = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'compliance_documents'
        indexes = [
            models.Index(fields=['category']),
        ]

    def __str__(self):
        return f"{self.title} - {self.category}"
