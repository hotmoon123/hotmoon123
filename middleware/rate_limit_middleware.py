"""
Rate Limiting Middleware
Applies rate limits to auth pages to prevent brute-force attacks.
"""
import time
import logging
from django.http import HttpResponse
from django.core.cache import cache

logger = logging.getLogger('middleware.rate_limit')

RATE_LIMITS = {
    '/login/':           (10, 900),   # 10 attempts per 15 min
    '/register/':        (5,  900),   # 5 registrations per 15 min
    '/forgot-password/': (3,  900),   # 3 resets per 15 min
}
DEFAULT_LIMIT = (200, 60)


class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Only POST requests on auth pages need rate limiting
        if request.method != 'POST':
            return self.get_response(request)

        path = request.path
        max_requests, window = DEFAULT_LIMIT
        for prefix, limits in RATE_LIMITS.items():
            if path.startswith(prefix):
                max_requests, window = limits
                break
        else:
            # Not a rate-limited path
            return self.get_response(request)

        client_ip = self._get_client_ip(request)
        cache_key = f'rate:{client_ip}:{path}'
        data = cache.get(cache_key)

        if data is None:
            cache.set(cache_key, {'count': 1, 'start': time.time()}, timeout=window)
        else:
            elapsed = time.time() - data['start']
            if elapsed > window:
                cache.set(cache_key, {'count': 1, 'start': time.time()}, timeout=window)
            elif data['count'] >= max_requests:
                retry_after = int(window - elapsed)
                logger.warning('Rate limit: ip=%s path=%s', client_ip, path)
                return HttpResponse(
                    '{"success":false,"errors":{"detail":"Too many requests. Please try again later."}}',
                    status=429,
                    content_type='application/json',
                    headers={'Retry-After': str(retry_after)},
                )
            else:
                data['count'] += 1
                cache.set(cache_key, data, timeout=int(window - elapsed))

        return self.get_response(request)

    def _get_client_ip(self, request):
        xff = request.META.get('HTTP_X_FORWARDED_FOR')
        return xff.split(',')[0].strip() if xff else request.META.get('REMOTE_ADDR', '0.0.0.0')
