"""
Leases App — Serializers

Input validation and output formatting for Lease API.
"""

from rest_framework import serializers
from django.utils import timezone
from datetime import timedelta
from .models import Lease, Invitation
from apps.properties.models import Property


class LeaseSerializer(serializers.ModelSerializer):
    """Serializer for Lease model (read operations)."""

    property_address = serializers.CharField(
        source="rental_property.address", read_only=True
    )
    property_unit = serializers.CharField(
        source="rental_property.unit_number", read_only=True
    )
    tenant_name = serializers.SerializerMethodField()
    landlord_name = serializers.SerializerMethodField()

    class Meta:
        model = Lease
        fields = [
            "id",
            "property",
            "property_address",
            "property_unit",
            "landlord",
            "landlord_name",
            "tenant",
            "tenant_name",
            "monthly_rent",
            "start_date",
            "end_date",
            "status",
            "signed_at",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "landlord",
            "tenant",
            "signed_at",
            "created_at",
            "updated_at",
        ]

    def get_tenant_name(self, obj):
        if obj.tenant:
            return f"{obj.tenant.first_name} {obj.tenant.last_name}"
        return None

    def get_landlord_name(self, obj):
        return f"{obj.landlord.first_name} {obj.landlord.last_name}"


class LeaseCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating a new lease."""

    class Meta:
        model = Lease
        fields = ["rental_property", "tenant", "monthly_rent", "start_date", "end_date"]
        extra_kwargs = {"rental_property": {"source": "property"}}

    def validate_rental_property(self, value):
        """Ensure property is vacant (no active lease)."""
        if value.status == "Leased":
            raise serializers.ValidationError(
                "This property already has an active lease."
            )
        if value.deleted_at is not None:
            raise serializers.ValidationError("This property no longer exists.")
        return value

    def validate(self, data):
        """Validate lease dates and check for overlaps."""
        start_date = data.get("start_date")
        end_date = data.get("end_date")
        rental_property = data.get("rental_property")

        if end_date <= start_date:
            raise serializers.ValidationError(
                {"end_date": "End date must be after start date."}
            )

        overlapping = Lease.objects.filter(
            rental_property=rental_property,
            status__in=["Pending", "Active"],
            deleted_at__isnull=True,
        ).filter(start_date__lte=end_date, end_date__gte=start_date)

        if self.instance:
            overlapping = overlapping.exclude(pk=self.instance.pk)

        if overlapping.exists():
            raise serializers.ValidationError(
                {
                    "start_date": "Lease dates overlap with an existing lease on this property."
                }
            )

        return data

    def validate_monthly_rent(self, value):
        if value <= 0:
            raise serializers.ValidationError("Monthly rent must be greater than zero.")
        return value


class LeaseUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating a lease."""

    class Meta:
        model = Lease
        fields = ["tenant", "monthly_rent", "start_date", "end_date", "status"]

    def validate(self, data):
        """Validate lease dates on update."""
        start_date = data.get("start_date", self.instance.start_date)
        end_date = data.get("end_date", self.instance.end_date)

        if end_date <= start_date:
            raise serializers.ValidationError(
                {"end_date": "End date must be after start date."}
            )

        return data


class InvitationSerializer(serializers.ModelSerializer):
    """Serializer for Invitation model."""

    lease_property = serializers.CharField(
        source="lease.rental_property.address", read_only=True
    )
    lease_unit = serializers.CharField(
        source="lease.rental_property.unit_number", read_only=True
    )

    class Meta:
        model = Invitation
        fields = [
            "id",
            "lease",
            "lease_property",
            "lease_unit",
            "email",
            "expires_at",
            "accepted_at",
            "created_at",
        ]
        read_only_fields = ["id", "expires_at", "accepted_at", "created_at"]
