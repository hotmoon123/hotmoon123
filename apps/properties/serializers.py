"""
Properties App — Serializers

Input validation and output formatting for Property API.
"""

from rest_framework import serializers
from .models import Building, Property


class BuildingSerializer(serializers.ModelSerializer):
    """Serializer for Building model."""

    class Meta:
        model = Building
        fields = ["id", "name", "address", "created_at"]
        read_only_fields = ["id", "created_at"]


class PropertySerializer(serializers.ModelSerializer):
    """Serializer for Property model."""

    building_name = serializers.CharField(
        source="building.name", read_only=True, allow_null=True
    )
    full_address = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = [
            "id",
            "unit_number",
            "address",
            "base_rent",
            "status",
            "building",
            "building_name",
            "full_address",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "status", "created_at", "updated_at"]

    def get_full_address(self, obj):
        if obj.building:
            return f"{obj.building.name} - {obj.address}"
        return obj.address


class PropertyCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating a new property."""

    class Meta:
        model = Property
        fields = ["unit_number", "address", "base_rent", "building"]

    def validate_base_rent(self, value):
        if value <= 0:
            raise serializers.ValidationError("Base rent must be greater than zero.")
        return value


class PropertyUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating a property."""

    class Meta:
        model = Property
        fields = ["unit_number", "address", "base_rent", "building"]

    def validate_base_rent(self, value):
        if value <= 0:
            raise serializers.ValidationError("Base rent must be greater than zero.")
        return value
