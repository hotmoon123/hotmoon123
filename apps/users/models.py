"""
Custom User Model — Rent & Lease Management System

This MUST be set as AUTH_USER_MODEL before running any migrations.
Uses email as the login identifier instead of username.
Supports two roles: 'landlord' and 'tenant'.
Implements soft delete via deleted_at field.
"""
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class SoftDeleteManager(models.Manager):
    """Default manager that excludes soft-deleted records."""

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class AllObjectsManager(models.Manager):
    """Manager that includes soft-deleted records."""
    pass


class CustomUserManager(BaseUserManager):
    """Manager for creating users with email as the identifier."""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_verified', True)
        extra_fields.setdefault('role', 'landlord')
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model using email for authentication.

    Fields align with database schema in docs/documents file.md:
    - email: unique login identifier (locked to lease for tenants)
    - role: 'landlord' or 'tenant' — determines portal routing
    - is_verified: set True after email verification
    - deleted_at: soft delete — NULL when active
    """

    ROLE_CHOICES = [
        ('landlord', 'Landlord'),
        ('tenant', 'Tenant'),
    ]

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30, blank=True, default='')
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)

    # Login with email, not username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']

    # Default manager excludes soft-deleted users
    objects = CustomUserManager()
    all_objects = AllObjectsManager()

    class Meta:
        db_table = 'users'
        indexes = [
            models.Index(fields=['email'], name='idx_users_email'),
            models.Index(fields=['role'], name='idx_users_role'),
            models.Index(fields=['deleted_at'], name='idx_users_deleted'),
        ]

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.role})'

    def soft_delete(self):
        """Soft delete — sets deleted_at timestamp instead of destroying."""
        self.deleted_at = timezone.now()
        self.is_active = False
        self.save(update_fields=['deleted_at', 'is_active', 'updated_at'])

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class LandlordProfile(models.Model):
    """
    Profile table specifically for Landlord users.
    Contains business, location, and banking details.
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='landlord_profile')
    
    # Business Details
    company_name = models.CharField(max_length=255, blank=True, default='')
    business_reg_no = models.CharField(max_length=100, blank=True, default='')
    tax_id = models.CharField(max_length=100, blank=True, default='')
    
    # Location
    address = models.TextField(blank=True, default='')
    city = models.CharField(max_length=100, blank=True, default='')
    state = models.CharField(max_length=100, blank=True, default='')
    country = models.CharField(max_length=100, blank=True, default='')
    postal_code = models.CharField(max_length=20, blank=True, default='')
    
    # Media & Bio
    profile_photo = models.CharField(max_length=500, blank=True, default='') # Path to stored file
    bio = models.TextField(blank=True, default='')
    
    # Banking (Sensitives should be securely handled, here for schema completion)
    bank_name = models.CharField(max_length=100, blank=True, default='')
    bank_account_no = models.CharField(max_length=100, blank=True, default='')
    bank_routing_no = models.CharField(max_length=100, blank=True, default='')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'landlords'

    def __str__(self):
        return f"Landlord Profile: {self.user.email}"


class TenantProfile(models.Model):
    """
    Profile table specifically for Tenant users.
    Contains personal identification, employment, and emergency contact details.
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='tenant_profile')
    
    # Personal Identification
    date_of_birth = models.DateField(null=True, blank=True)
    national_id_number = models.CharField(max_length=100, blank=True, default='')
    id_document = models.CharField(max_length=500, blank=True, default='') # Path to uploaded doc
    profile_photo = models.CharField(max_length=500, blank=True, default='') # Path to stored file
    
    # Employment & Finance
    employer_name = models.CharField(max_length=255, blank=True, default='')
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Emergency Contact
    emergency_contact_name = models.CharField(max_length=100, blank=True, default='')
    emergency_contact_phone = models.CharField(max_length=30, blank=True, default='')
    emergency_contact_relation = models.CharField(max_length=50, blank=True, default='')
    
    # Rental History
    previous_address = models.TextField(blank=True, default='')
    previous_landlord_name = models.CharField(max_length=100, blank=True, default='')
    previous_landlord_phone = models.CharField(max_length=30, blank=True, default='')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tenants'

    def __str__(self):
        return f"Tenant Profile: {self.user.email}"
