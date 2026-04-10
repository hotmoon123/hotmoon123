"""
Properties App — API Views (Layer 5)

RESTful CRUD operations for Buildings and Properties.
Follows the 9-layer architecture: Views → Business Rules → Business Logic → Data Access.
"""

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone

from .models import Building, Property
from .serializers import (
    BuildingSerializer,
    PropertySerializer,
    PropertyCreateSerializer,
    PropertyUpdateSerializer,
)


class BuildingViewSet(viewsets.ModelViewSet):
    """
    API endpoints for managing buildings.

    Endpoints:
    - GET    /api/v1/properties/buildings/         - List all buildings
    - POST   /api/v1/properties/buildings/         - Create building
    - GET    /api/v1/properties/buildings/{id}/    - Get building
    - PUT    /api/v1/properties/buildings/{id}/    - Update building
    - DELETE /api/v1/properties/buildings/{id}/    - Delete building
    """

    serializer_class = BuildingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter buildings to only show landlord's own buildings."""
        return Building.objects.filter(
            landlord=self.request.user, deleted_at__isnull=True
        )

    def perform_create(self, serializer):
        """Set landlord to current user on create."""
        serializer.save(landlord=self.request.user)


class PropertyViewSet(viewsets.ModelViewSet):
    """
    API endpoints for managing properties.

    Endpoints:
    - GET    /api/v1/properties/                    - List all properties
    - POST   /api/v1/properties/                    - Create property
    - GET    /api/v1/properties/{id}/               - Get property
    - PUT    /api/v1/properties/{id}/               - Update property
    - DELETE /api/v1/properties/{id}/               - Delete property (soft delete)
    - GET    /api/v1/properties/stats/              - Get property statistics
    """

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter properties to only show landlord's own properties."""
        return Property.objects.filter(
            landlord=self.request.user, deleted_at__isnull=True
        ).select_related("building")

    def get_serializer_class(self):
        """Return appropriate serializer based on action."""
        if self.action == "create":
            return PropertyCreateSerializer
        elif self.action in ["update", "partial_update"]:
            return PropertyUpdateSerializer
        return PropertySerializer

    def perform_create(self, serializer):
        """Set landlord to current user on create."""
        serializer.save(landlord=self.request.user)

    def perform_destroy(self, instance):
        """Soft delete instead of hard delete."""
        instance.deleted_at = timezone.now()
        instance.save()

    @action(detail=False, methods=["get"])
    def stats(self, request):
        """
        GET /api/v1/properties/stats/

        Returns property portfolio statistics for the landlord dashboard.
        """
        properties = self.get_queryset()
        total = properties.count()
        vacant = properties.filter(status="Vacant").count()
        leased = properties.filter(status="Leased").count()

        total_rent = sum(p.base_rent for p in properties.filter(status="Leased"))
        expected_rent = sum(p.base_rent for p in properties)

        occupancy_rate = (leased / total * 100) if total > 0 else 0

        return Response(
            {
                "total_properties": total,
                "vacant": vacant,
                "leased": leased,
                "occupancy_rate": round(occupancy_rate, 1),
                "total_rent_collected": float(total_rent),
                "expected_monthly_rent": float(expected_rent),
            }
        )
