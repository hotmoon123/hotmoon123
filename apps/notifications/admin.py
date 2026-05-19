from django.contrib import admin
from .models import Notification, ActivityLog

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'recipient_type', 'type', 'is_read', 'created_at')
    list_filter = ('recipient_type', 'type', 'is_read', 'created_at')
    search_fields = ('title', 'message')
    readonly_fields = ('created_at',)

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('actor_type', 'action', 'related_table', 'created_at')
    list_filter = ('actor_type', 'action', 'created_at')
    search_fields = ('description', 'action')
    readonly_fields = ('created_at',)
