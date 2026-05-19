"""
Dual-model authentication middleware.

Replaces Django's AuthenticationMiddleware. Resolves request.user from session
using both user_id AND user_type to avoid ID collision (landlord id=1 and
tenant id=1 both exist independently).

Store _auth_user_type in session after login/register to indicate which
model to use when loading the user.
"""
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import SESSION_KEY
from django.utils.functional import SimpleLazyObject
from .models import Landlord, Tenant


def get_user(request):
    """
    Resolve request.user from session using user_type to distinguish
    between Landlord and Tenant models (both may have same numeric ID).
    """
    try:
        user_id = int(request.session.get(SESSION_KEY, 0))
        user_type = request.session.get('_auth_user_type', '')
    except (ValueError, TypeError):
        return AnonymousUser()

    if not user_id:
        return AnonymousUser()

    if user_type == 'landlord':
        try:
            user = Landlord.objects.get(pk=user_id)
            if user.is_active:
                return user
        except Landlord.DoesNotExist:
            pass
    elif user_type == 'tenant':
        try:
            user = Tenant.objects.get(pk=user_id)
            if user.is_active:
                return user
        except Tenant.DoesNotExist:
            pass

    return AnonymousUser()


class DualModelAuthMiddleware:
    """
    Replaces Django's AuthenticationMiddleware to support two independent
    user models (Landlord and Tenant) with session-based authentication.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user = SimpleLazyObject(lambda: get_user(request))
        response = self.get_response(request)
        return response
