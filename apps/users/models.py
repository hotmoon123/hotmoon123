"""
Custom User Models — Rent & Lease Management System

Two completely independent models:
- Landlord(AbstractBaseUser, PermissionsMixin) → landlord_accounts table
- Tenant(AbstractBaseUser) → tenant_accounts table

No MTI, no shared users table. Both stored entirely in their own tables.
"""
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
import hashlib


class LandlordManager(BaseUserManager):
    """Manager for creating landlords with email as the identifier."""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class Landlord(AbstractBaseUser, PermissionsMixin):
    """Landlord user model — stored entirely in landlord_accounts table."""
    email           = models.EmailField(max_length=255, unique=True)
    first_name      = models.CharField(max_length=150, default='')
    last_name       = models.CharField(max_length=150, default='')
    phone_number    = models.CharField(max_length=30, default='')
    company_name    = models.CharField(max_length=255, default='')
    business_reg_no = models.CharField(max_length=100, default='')
    tax_id          = models.CharField(max_length=100, default='')
    address         = models.CharField(max_length=500, default='')
    city            = models.CharField(max_length=100, default='')
    state           = models.CharField(max_length=100, default='')
    country         = models.CharField(max_length=100, default='')
    postal_code     = models.CharField(max_length=20, default='')
    profile_photo   = models.ImageField(upload_to='landlord/photos/', null=True, blank=True)
    bio             = models.TextField(default='')
    bank_name       = models.CharField(max_length=255, default='')
    bank_account_no = models.CharField(max_length=100, default='')
    bank_routing_no = models.CharField(max_length=100, default='')
    is_verified     = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    created_at      = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = LandlordManager()

    class Meta:
        db_table = 'landlord_accounts'

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()


class TenantManager(BaseUserManager):
    """Manager for creating tenants with email as the identifier."""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class Tenant(AbstractBaseUser):
    """Tenant user model — stored entirely in tenant_accounts table."""
    email                       = models.EmailField(max_length=255, unique=True)
    first_name                  = models.CharField(max_length=150, default='')
    last_name                   = models.CharField(max_length=150, default='')
    phone_number                = models.CharField(max_length=30, default='')
    date_of_birth               = models.DateField(null=True, blank=True)
    national_id_number          = models.CharField(max_length=100, default='')
    id_document                 = models.FileField(upload_to='tenant/docs/', null=True, blank=True)
    employer_name               = models.CharField(max_length=255, default='')
    monthly_income              = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    emergency_contact_name      = models.CharField(max_length=255, default='')
    emergency_contact_phone     = models.CharField(max_length=30, default='')
    emergency_contact_relation  = models.CharField(max_length=100, default='')
    profile_photo               = models.ImageField(upload_to='tenant/photos/', null=True, blank=True)
    previous_address            = models.CharField(max_length=500, default='')
    previous_landlord_name      = models.CharField(max_length=255, default='')
    previous_landlord_phone     = models.CharField(max_length=30, default='')
    is_verified                 = models.BooleanField(default=False)
    is_active                   = models.BooleanField(default=True)
    is_staff                    = models.BooleanField(default=False)
    is_superuser                = models.BooleanField(default=False)
    created_at                  = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = TenantManager()

    class Meta:
        db_table = 'tenant_accounts'

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


class PasswordResetToken(models.Model):
    """Secure tokens for password reset flow (supports both user types)."""
    USER_TYPE_CHOICES = [
        ('landlord', 'Landlord'),
        ('tenant', 'Tenant'),
    ]

    user_type   = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    user_id     = models.BigIntegerField()
    token_hash  = models.CharField(max_length=255, unique=True)
    expires_at  = models.DateTimeField()
    used_at     = models.DateTimeField(null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'password_reset_tokens'
        indexes = [
            models.Index(fields=['token_hash']),
            models.Index(fields=['user_type', 'user_id']),
        ]

    def __str__(self):
        return f"Token for {self.user_type} {self.user_id}"

    @property
    def is_expired(self):
        from django.utils import timezone
        return timezone.now() > self.expires_at

    @property
    def is_used(self):
        return self.used_at is not None
