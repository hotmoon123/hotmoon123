from django.contrib import admin
from .models import Document, ComplianceDocument

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_type', 'landlord', 'tenant', 'uploaded_at')
    list_filter = ('file_type', 'uploaded_at')
    search_fields = ('title', 'file_path')
    readonly_fields = ('uploaded_at',)

@admin.register(ComplianceDocument)
class ComplianceDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'landlord', 'is_mandatory', 'valid_until')
    list_filter = ('category', 'is_mandatory', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
