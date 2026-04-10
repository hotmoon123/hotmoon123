"""
Users App — DRF Serializers (Layer 5 — API Boundary)

Serializers define the exact shape of data the API accepts and returns.
They validate types, required fields, and format before data reaches business logic.
"""
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.Serializer):
    """Validates registration input — never auto-creates the user."""
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(min_length=8, write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=['landlord', 'tenant'])
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=30, required=False, default='')

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
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class UserProfileSerializer(serializers.ModelSerializer):
    """Read-only user profile data returned after authentication."""
    class Meta:
        model = User
        fields = ['id', 'email', 'role', 'first_name', 'last_name',
                  'phone_number', 'is_verified', 'created_at']
        read_only_fields = fields


class ForgotPasswordSerializer(serializers.Serializer):
    """Validates forgot password request — only needs email."""
    email = serializers.EmailField()


class ResetPasswordSerializer(serializers.Serializer):
    """Validates password reset with token."""
    token = serializers.CharField()
    new_password = serializers.CharField(min_length=8)
    confirm_password = serializers.CharField()

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({'confirm_password': 'Passwords do not match.'})
        return data


class VerifyEmailSerializer(serializers.Serializer):
    """Validates email verification token."""
    token = serializers.CharField()
