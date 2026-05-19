"""
Role Authorization Middleware
Prevents tenants from accessing landlord pages and vice versa.
Replaces the former API-only IDOR middleware with page-level enforcement.
"""
import logging
from django.shortcuts import redirect

from apps.users.models import Landlord, Tenant

logger = logging.getLogger('middleware.authorization')

LANDLORD_ONLY = ['/landlord/']
TENANT_ONLY   = ['/tenant/']
PUBLIC_PATHS  = ['/login/', '/register/', '/forgot-password/', '/reset-password/',
                 '/verify-email/', '/admin/', '/static/', '/media/', '/']


class RoleAuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path

        # Skip for public/static paths
        if any(path.startswith(p) for p in PUBLIC_PATHS):
            return self.get_response(request)

        if not request.user.is_authenticated:
            return redirect(f'/login/?next={path}')

        is_landlord = isinstance(request.user, Landlord)
        is_tenant = isinstance(request.user, Tenant)

        # Block tenants from landlord pages
        if any(path.startswith(p) for p in LANDLORD_ONLY) and not is_landlord:
            logger.warning('Role block: tenant=%s tried landlord path=%s', request.user.email, path)
            return redirect('/tenant/dashboard/')

        # Block landlords from tenant pages
        if any(path.startswith(p) for p in TENANT_ONLY) and not is_tenant:
            logger.warning('Role block: landlord=%s tried tenant path=%s', request.user.email, path)
            return redirect('/landlord/dashboard/')

        return self.get_response(request)
