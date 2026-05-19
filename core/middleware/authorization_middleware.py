"""
IDOR Authorization Middleware

Prevents Insecure Direct Object Reference attacks at the middleware level.
This is the FIRST line of IDOR defense — the SECOND line is query-level
scoping in every ViewSet's get_queryset() method.

Both lines must exist independently — defense in depth.
"""
import logging
from django.http import JsonResponse

from apps.users.models import Landlord, Tenant

logger = logging.getLogger('middleware.authorization')


class IDORAuthorizationMiddleware:
    """
    Base IDOR protection at the middleware level.

    For Phase 1, this provides the framework. As more apps are built,
    resource-specific ownership checks are added here.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip for unauthenticated requests (handled by DRF permissions)
        if not hasattr(request, 'user') or not request.user.is_authenticated:
            return self.get_response(request)

        # Skip for non-API requests
        if not request.path.startswith('/api/'):
            return self.get_response(request)

        # Role-based path restrictions
        if not self._check_role_access(request):
            logger.warning(
                'IDOR blocked: user=%s kind=%s path=%s',
                request.user.email,
                'landlord' if isinstance(request.user, Landlord) else (
                    'tenant' if isinstance(request.user, Tenant) else 'unknown'
                ),
                request.path,
            )
            return JsonResponse(
                {'errors': {'detail': 'You do not have permission to access this resource.'}},
                status=403
            )

        return self.get_response(request)

    def _check_role_access(self, request):
        """
        Enforce that landlord-only paths cannot be accessed by tenants
        and vice versa.
        """
        path = request.path
        is_landlord = isinstance(request.user, Landlord)
        is_tenant = isinstance(request.user, Tenant)

        # Landlord-only API paths
        landlord_only = [
            '/api/v1/properties/',
            '/api/v1/automation/',
            '/api/v1/analytics/',
        ]

        # Tenant-only API paths
        tenant_only = [
            '/api/v1/financials/pay/',
            '/api/v1/financials/auto-pay/',
        ]

        for prefix in landlord_only:
            if path.startswith(prefix) and not is_landlord:
                return False

        for prefix in tenant_only:
            if path.startswith(prefix) and not is_tenant:
                return False

        return True
