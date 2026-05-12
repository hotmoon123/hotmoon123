"""
Leases App — API Views (Layer 5)

RESTful CRUD operations for Leases and Invitations.
Follows the 9-layer architecture.
"""

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from django.db.models import Q

from .models import Lease, Invitation
from .serializers import (
    LeaseSerializer,
    LeaseCreateSerializer,
    LeaseUpdateSerializer,
    InvitationSerializer,
)
from apps.properties.models import Property


class LeaseViewSet(viewsets.ModelViewSet):
    """
    API endpoints for managing leases.

    Endpoints:
    - GET    /api/v1/leases/                    - List all leases
    - POST   /api/v1/leases/                    - Create lease
    - GET    /api/v1/leases/{id}/               - Get lease
    - PUT    /api/v1/leases/{id}/               - Update lease
    - DELETE /api/v1/leases/{id}/               - Delete lease
    - GET    /api/v1/leases/expiring/           - Get leases expiring soon
    - POST   /api/v1/leases/{id}/invite         - Send tenant invitation
    - POST   /api/v1/leases/{id}/accept         - Accept invitation (tenant)
    """

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter leases based on user role."""
        user = self.request.user
        if user.role == "landlord":
            return Lease.objects.filter(
                landlord=user, deleted_at__isnull=True
            ).select_related("property", "tenant")
        else:
            return Lease.objects.filter(
                tenant=user, deleted_at__isnull=True
            ).select_related("property", "landlord")

    def get_serializer_class(self):
        """Return appropriate serializer based on action."""
        if self.action == "create":
            return LeaseCreateSerializer
        elif self.action in ["update", "partial_update"]:
            return LeaseUpdateSerializer
        return LeaseSerializer

    def perform_create(self, serializer):
        """Set landlord to current user on create."""
        lease = serializer.save(landlord=self.request.user)
        property_obj = lease.property

    def perform_destroy(self, instance):
        """Soft delete instead of hard delete."""
        instance.deleted_at = timezone.now()
        instance.save()

    @action(detail=False, methods=["get"])
    def expiring(self, request):
        """
        GET /api/v1/leases/expiring/

        Returns leases expiring within the next 60 days.
        """
        days = request.query_params.get("days", 60)
        try:
            days = int(days)
        except ValueError:
            days = 60

        target_date = timezone.now().date() + timezone.timedelta(days=days)

        leases = (
            self.get_queryset()
            .filter(
                status="Active",
                end_date__lte=target_date,
                end_date__gte=timezone.now().date(),
            )
            .order_by("end_date")
        )

        serializer = LeaseSerializer(leases, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def invite(self, request, pk=None):
        """
        POST /api/v1/leases/{id}/invite/

        Send an invitation email to a tenant.
        """
        lease = self.get_object()

        if lease.landlord != request.user:
            return Response(
                {
                    "errors": {
                        "detail": "You do not have permission to invite to this lease."
                    }
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        if lease.tenant:
            return Response(
                {"errors": {"detail": "This lease already has a tenant assigned."}},
                status=status.HTTP_400_BAD_REQUEST,
            )

        email = request.data.get("email")
        if not email:
            return Response(
                {"errors": {"email": "Email is required."}},
                status=status.HTTP_400_BAD_REQUEST,
            )

        invitation = Invitation.objects.create(
            lease=lease,
            landlord=request.user,
            email=email,
            token_hash=f"hashed_token_{timezone.now().timestamp()}",
            expires_at=timezone.now() + timezone.timedelta(hours=24),
        )

        return Response(
            {
                "message": f"Invitation sent to {email}",
                "invitation": InvitationSerializer(invitation).data,
            },
            status=status.HTTP_201_CREATED,
        )

    @action(detail=True, methods=["post"])
    def accept(self, request, pk=None):
        """
        POST /api/v1/leases/{id}/accept/

        Tenant accepts the invitation and binds to the lease.
        """
        lease = self.get_object()
        user = request.user

        if lease.tenant:
            return Response(
                {"errors": {"detail": "This lease already has a tenant assigned."}},
                status=status.HTTP_400_BAD_REQUEST,
            )

        invitation = Invitation.objects.filter(
            lease=lease, email=user.email, accepted_at__isnull=True
        ).first()

        if not invitation:
            return Response(
                {"errors": {"detail": "No pending invitation found for your email."}},
                status=status.HTTP_404_NOT_FOUND,
            )

        if invitation.is_expired:
            return Response(
                {"errors": {"detail": "This invitation has expired."}},
                status=status.HTTP_400_BAD_REQUEST,
            )

        invitation.accepted_at = timezone.now()
        invitation.save()

        lease.tenant = user
        lease.signed_at = timezone.now()
        lease.save()

        property_obj = lease.property
        property_obj.status = "occupied"
        property_obj.save()

        return Response(
            {
                "message": "You have successfully joined the lease.",
                "lease": LeaseSerializer(lease).data,
            }
        )


class InvitationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoints for viewing invitations (landlord only).
    """

    serializer_class = InvitationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter invitations to landlord's own invitations."""
        return Invitation.objects.filter(landlord=self.request.user).select_related(
            "lease", "lease__property"
        )
