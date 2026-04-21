"""
Request Logging Middleware

Logs every request to the console with timing information.
In production, this feeds into the audit_log table.
Runs on EVERY request — the system's surveillance camera.
"""
import time
import logging

logger = logging.getLogger('middleware.logging')


class RequestLoggingMiddleware:
    """Logs method, path, user, status code, and response time for every request."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        duration_ms = (time.time() - start_time) * 1000
        user = getattr(request, 'user', None)
        user_display = user.email if user and user.is_authenticated else 'anonymous'

        logger.info(
            '%s %s | user=%s | status=%s | %.0fms',
            request.method,
            request.path,
            user_display,
            response.status_code,
            duration_ms,
        )

        return response
