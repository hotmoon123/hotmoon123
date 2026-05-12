"""
Users App — DRF Serializers (Layer 5 — API Boundary)

Serializers define the exact shape of data the API accepts and returns.
They validate types, required fields, and format before data reaches business logic.

Three serializer groups:
  - Auth          → RegisterSerializer, LoginSerializer, etc.
  - Profiles      → LandlordProfileSerializer, TenantProfileSerializer
  - Unified Read  → UserProfileSerializer (nests correct profile by role)
"""
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import LandlordProfile, TenantProfile

User = get_user_model()


# ─── AUTH SERIALIZERS ────────────────────────────────────────────

class RegisterSerializer(serializers.Serializer):
    """Validates registration input — never auto-creates the user."""
    email            = serializers.EmailField(max_length=255)
    password         = serializers.CharField(min_length=8, write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    role             = serializers.ChoiceField(choices=['landlord', 'tenant'])
    first_name       = serializers.CharField(max_length=100)
    last_name        = serializers.CharField(max_length=100)
    phone_number     = serializers.CharField(max_length=30, required=False, default='')

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({'confirm_password': 'Passwords do not match.'})
        return data

    def validate_email(self, value):
        if User.objects.filter(email=value.lower().strip()).exists():
            raise serializers.ValidationError('An account with this email already exists.')
        return value.lower().strip()


class LoginSerializer(serializers.Serializer):
    """Validates login input."""
    email    = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class ForgotPasswordSerializer(serializers.Serializer):
    """Validates forgot password request — only needs email."""
    email = serializers.EmailField()


class ResetPasswordSerializer(serializers.Serializer):
    """Validates password reset with token."""
    token            = serializers.CharField()
    new_password     = serializers.CharField(min_length=8)
    confirm_password = serializers.CharField()

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({'confirm_password': 'Passwords do not match.'})
        return data


class VerifyEmailSerializer(serializers.Serializer):
    """Validates email verification token."""
    token = serializers.CharField()


# ─── PROFILE SERIALIZERS ─────────────────────────────────────────

class LandlordProfileSerializer(serializers.ModelSerializer):
    """
    Read/write serializer for the `landlords` table.
    Used in profile update endpoints and nested inside UserProfileSerializer.
    """
    class Meta:
        model  = LandlordProfile
        fields = [
            'company_name', 'business_reg_no', 'tax_id',
            'address', 'city', 'state', 'country', 'postal_code',
            'profile_photo', 'bio',
            'bank_name', 'bank_account_no', 'bank_routing_no',
            'created_at', 'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class TenantProfileSerializer(serializers.ModelSerializer):
    """
    Read/write serializer for the `tenants` table.
    Used in profile update endpoints and nested inside UserProfileSerializer.
    """
    class Meta:
        model  = TenantProfile
        fields = [
            'date_of_birth', 'national_id_number', 'id_document',
            'employer_name', 'monthly_income',
            'emergency_contact_name', 'emergency_contact_phone', 'emergency_contact_relation',
            'profile_photo',
            'previous_address', 'previous_landlord_name', 'previous_landlord_phone',
            'created_at', 'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


# ─── UNIFIED USER + PROFILE SERIALIZER ──────────────────────────

class UserProfileSerializer(serializers.ModelSerializer):
    """
    Read-only serializer returned after authentication (login, /me/ endpoint).

    Nests the correct profile object based on `role`:
      - role='landlord'  →  includes `landlord_profile` from the `landlords` table
      - role='tenant'    →  includes `tenant_profile`   from the `tenants`   table
    """
    landlord_profile = LandlordProfileSerializer(read_only=True)
    tenant_profile   = TenantProfileSerializer(read_only=True)

    class Meta:
        model  = User
        fields = [
            'id', 'email', 'role',
            'first_name', 'last_name', 'phone_number',
            'is_verified', 'created_at',
            'landlord_profile',   # populated only if role='landlord', else null
            'tenant_profile',     # populated only if role='tenant',   else null
        ]
        read_only_fields = fields

