from django.contrib import admin
from .models import Notice

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'landlord', 'is_pinned', 'expires_at', 'created_at')
    list_filter = ('is_pinned', 'created_at', 'expires_at')
    search_fields = ('title', 'body')
    readonly_fields = ('created_at', 'updated_at')
