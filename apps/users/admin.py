from django.contrib import admin
from .models import Landlord, Tenant, PasswordResetToken


@admin.register(Landlord)
class LandlordAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'created_at')
    list_filter = ('is_active', 'is_staff', 'created_at')
    search_fields = ('email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('id', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number', 'profile_photo')}),
        ('Business', {'fields': ('company_name', 'business_reg_no', 'tax_id')}),
        ('Address', {'fields': ('address', 'city', 'state', 'country', 'postal_code')}),
        ('Bank/MoMo', {'fields': ('bank_name', 'bank_account_no', 'bank_routing_no', 'momo_number')}),
        ('Status', {'fields': ('is_verified', 'is_active', 'is_staff', 'is_superuser')}),
        ('Important', {'fields': ('created_at', 'last_login')}),
    )
    readonly_fields = ('id', 'created_at', 'last_login')
    ordering = ('-created_at',)


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('id', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number', 'date_of_birth', 'profile_photo')}),
        ('Identity', {'fields': ('national_id_number', 'id_document')}),
        ('Employment', {'fields': ('employer_name', 'monthly_income')}),
        ('Emergency Contact', {'fields': ('emergency_contact_name', 'emergency_contact_phone', 'emergency_contact_relation')}),
        ('Rental History', {'fields': ('previous_address', 'previous_landlord_name', 'previous_landlord_phone')}),
        ('Status', {'fields': ('is_verified', 'is_active')}),
        ('Important', {'fields': ('created_at', 'last_login')}),
    )
    readonly_fields = ('id', 'created_at', 'last_login')
    ordering = ('-created_at',)


@admin.register(PasswordResetToken)
class PasswordResetTokenAdmin(admin.ModelAdmin):
    list_display = ('user_type', 'user_id', 'is_expired', 'is_used', 'created_at')
    list_filter = ('user_type', 'created_at')
    search_fields = ('user_id', 'token_hash')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
