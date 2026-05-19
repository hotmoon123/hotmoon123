"""Canonical user models live in apps.users.models — import from there."""
from apps.users.models import (  # noqa: F401
    AllObjectsManager,
    CustomUser,
    CustomUserManager,
    Landlord,
    SoftDeleteManager,
    Tenant,
)

__all__ = [
    'AllObjectsManager',
    'CustomUser',
    'CustomUserManager',
    'Landlord',
    'SoftDeleteManager',
    'Tenant',
]
