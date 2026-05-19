from django.contrib import admin
from .models import AutomationRule

@admin.register(AutomationRule)
class AutomationRuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'trigger_event', 'action', 'landlord', 'is_active', 'last_run_at')
    list_filter = ('trigger_event', 'action', 'is_active', 'created_at')
    search_fields = ('name', 'conditions')
    readonly_fields = ('created_at', 'updated_at', 'last_run_at')
