from django.contrib import admin
from .models import Inspection

@admin.register(Inspection)
class InspectionAdmin(admin.ModelAdmin):
    list_display = ('type', 'condition', 'landlord', 'tenant', 'property', 'conducted_at')
    list_filter = ('type', 'condition', 'created_at')
    search_fields = ('notes',)
    readonly_fields = ('created_at',)
