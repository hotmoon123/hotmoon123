from rest_framework import viewsets, permissions
from .models import Building, Property
from .serializers import BuildingSerializer, PropertySerializer
from apps.users.permissions import IsLandlord

class PropertyViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing properties.
    Automatically restricts access based on landlord ownership.
    """
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticated, IsLandlord]

    def get_queryset(self):
        # Layer 5 IDOR check: Only return properties owned by the authenticated landlord
        return Property.objects.filter(landlord=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        # Automatically assign the logged-in landlord as owner
        serializer.save(landlord=self.request.user)

class BuildingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing buildings.
    """
    serializer_class = BuildingSerializer
    permission_classes = [permissions.IsAuthenticated, IsLandlord]

    def get_queryset(self):
        return Building.objects.filter(landlord=self.request.user).order_by('name')

    def perform_create(self, serializer):
        serializer.save(landlord=self.request.user)
