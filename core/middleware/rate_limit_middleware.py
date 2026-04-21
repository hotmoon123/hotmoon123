"""
Rate Limiting Middleware

Two-tier rate limiting as defined in the security architecture:
- Tier 1 (this middleware): Broad, global rate limit per IP/user
- Tier 2 (per-view decorators): Specific limits on sensitive endpoints

Uses Django's cache framework (LocMem for dev, Redis for production).
"""
import time
import logging
from django.http import JsonResponse
from django.core.cache import cache

logger = logging.getLogger('middleware.rate_limit')

# Rate limit configuration
RATE_LIMITS = {
    # path_prefix: (max_requests, window_seconds)
    '/api/v1/auth/login': (10, 900),          # 10 attempts per 15 minutes
    '/api/v1/auth/register': (5, 900),        # 5 registrations per 15 minutes
    '/api/v1/auth/forgot-password': (3, 900), # 3 reset requests per 15 minutes
}
DEFAULT_LIMIT = (200, 60)  # 200 requests per minute (global default)


class RateLimitMiddleware:
    """Per-IP rate limiting with endpoint-specific overrides."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip rate limiting for non-API requests (static files, etc.)
        if not request.path.startswith('/api/'):
            return self.get_response(request)

        client_ip = self._get_client_ip(request)

        # Find the most specific rate limit for this path
        max_requests, window = DEFAULT_LIMIT
        for path_prefix, limits in RATE_LIMITS.items():
            if request.path.startswith(path_prefix):
                max_requests, window = limits
                break

        # Build cache key
        cache_key = f'rate_limit:{client_ip}:{request.path}'

        # Get current request count
        request_data = cache.get(cache_key)

        if request_data is None:
            # First request in this window
            cache.set(cache_key, {'count': 1, 'start': time.time()}, timeout=window)
        else:
            elapsed = time.time() - request_data['start']
            if elapsed > window:
                # Window expired, reset
                cache.set(cache_key, {'count': 1, 'start': time.time()}, timeout=window)
            elif request_data['count'] >= max_requests:
                # Rate limit exceeded
                retry_after = int(window - elapsed)
                logger.warning(
                    'Rate limit exceeded: ip=%s path=%s count=%d limit=%d',
                    client_ip, request.path, request_data['count'], max_requests
                )
                return JsonResponse(
                    {
                        'errors': {
                            'detail': 'Too many requests. Please try again later.',
                        },
                        'retry_after': retry_after,
                    },
                    status=429,
                    headers={'Retry-After': str(retry_after)},
                )
            else:
                # Increment counter
                request_data['count'] += 1
                remaining = int(window - elapsed)
                cache.set(cache_key, request_data, timeout=remaining)

        return self.get_response(request)

    def _get_client_ip(self, request):
        """Extract client IP, accounting for reverse proxy headers."""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0].strip()
        return request.META.get('REMOTE_ADDR', '0.0.0.0')
