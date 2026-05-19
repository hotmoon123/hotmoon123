"""
Email-based authentication backend for dual-model auth system.
Authenticates against both Landlord and Tenant tables.
"""
from django.contrib.auth.backends import BaseBackend
from .models import Landlord, Tenant


class EmailBackend(BaseBackend):
    """Authenticate using email against Landlord or Tenant models."""

    def authenticate(self, request, email=None, password=None, **kwargs):
        if not email or not password:
            return None

        email = email.lower().strip()

        # Try Landlord first
        try:
            user = Landlord.objects.get(email=email)
            if user.check_password(password) and user.is_active:
                return user
        except Landlord.DoesNotExist:
            pass

        # Then try Tenant
        try:
            user = Tenant.objects.get(email=email)
            if user.check_password(password) and user.is_active:
                return user
        except Tenant.DoesNotExist:
            pass

        return None

    def get_user(self, user_id):
        """
        Retrieve user by pk. Checks Landlord first (primary AUTH_USER_MODEL),
        then Tenant. DualModelAuthMiddleware will use session _auth_user_type
        to ensure correct type is loaded.
        """
        try:
            return Landlord.objects.get(pk=user_id)
        except Landlord.DoesNotExist:
            pass

        try:
            return Tenant.objects.get(pk=user_id)
        except Tenant.DoesNotExist:
            pass

        return None
