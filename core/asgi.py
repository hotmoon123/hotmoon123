"""
ASGI config for Rent & Lease Management System.

Supports both HTTP and WebSocket protocols via Django Channels.
HTTP requests are handled by Django's standard ASGI handler.
WebSocket connections are routed to Channels consumers.
"""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Initialize Django ASGI application early to populate AppRegistry
django_asgi_app = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    # WebSocket routing will be added in Phase 5:
    # 'websocket': AuthMiddlewareStack(
    #     URLRouter(
    #         chat.routing.websocket_urlpatterns +
    #         notifications.routing.websocket_urlpatterns
    #     )
    # ),
})
