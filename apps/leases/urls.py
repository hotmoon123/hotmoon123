"""
Leases App — URL Configuration

All lease and invitation endpoints under /api/v1/leases/
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = "leases"

router = DefaultRouter()
router.register(r"", views.LeaseViewSet, basename="lease")

urlpatterns = [
    path("", include(router.urls)),
]
