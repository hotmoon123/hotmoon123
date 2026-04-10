"""
Properties App — URL Configuration

All property and building endpoints under /api/v1/properties/
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = "properties"

router = DefaultRouter()
router.register(r"buildings", views.BuildingViewSet, basename="building")
router.register(r"", views.PropertyViewSet, basename="property")

urlpatterns = [
    path("", include(router.urls)),
]
