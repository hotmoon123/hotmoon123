"""
Users App — Custom DRF Permissions

Role-based permission classes used across all viewsets.
These complement the IDOR middleware — they check WHO the user is.
The middleware checks WHAT they're accessing.
"""
from rest_framework.permissions import BasePermission


class IsLandlord(BasePermission):
    """Allows access only to users with role='landlord'."""
    message = 'This action is only available to landlords.'

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == 'landlord'
        )


class IsTenant(BasePermission):
    """Allows access only to users with role='tenant'."""
    message = 'This action is only available to tenants.'

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == 'tenant'
        )


class IsVerified(BasePermission):
    """Allows access only to users who have verified their email."""
    message = 'Please verify your email before accessing this resource.'

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_verified
        )
