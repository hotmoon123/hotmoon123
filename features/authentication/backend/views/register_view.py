"""
Registration View — Single Responsibility
Handles HTTP request/response for user registration only.
Delegates business logic to service layer.
"""
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.exceptions import ValidationError
import logging

from features.authentication.backend.serializers import RegisterSerializer, UserProfileSerializer
from features.authentication.backend.business_rules.validate_password import validate_password_strength
from features.authentication.backend.business_rules.validate_role import validate_role
from features.authentication.backend.business_rules.validate_name import validate_name_not_empty
from features.authentication.backend.business_logic.create_user import create_user
from features.authentication.backend.business_logic.send_emails import send_verification_email_async

logger = logging.getLogger(__name__)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    """
    POST /api/v1/auth/register/
    
    Creates a new user account and queues verification email.
    Single responsibility: Handle HTTP request/response only.
    Delegates validation and business logic to appropriate layers.
    """
    # Step 1: Validate input via serializer
    serializer = RegisterSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            {'errors': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    data = serializer.validated_data

    # Step 2: Apply business rules
    try:
        validate_password_strength(data['password'])
        validate_role(data['role'])
        validate_name_not_empty(data['first_name'], data['last_name'])
    except ValidationError as e:
        logger.warning(f"Business rule validation failed: {e.message}")
        return Response(
            {'errors': {'detail': str(e.message)}},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Step 3: Execute business logic
    try:
        user = create_user(
            email=data['email'],
            password=data['password'],
            role=data['role'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            phone_number=data.get('phone_number', ''),
        )
    except Exception as e:
        logger.error(f"User creation failed: {e}")
        return Response(
            {'errors': {'detail': 'Failed to create account. Please try again.'}},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    # Step 4: Send verification email (async, non-blocking)
    try:
        send_verification_email_async.delay(user.id)
        logger.info(f"Verification email queued for user {user.id}")
    except Exception as e:
        # Email failure should not block registration
        logger.error(f"Failed to queue verification email for user {user.id}: {e}")

    # Step 5: Return response
    return Response(
        {
            'message': 'Account created. Please check your email to verify your account.',
            'user': UserProfileSerializer(user).data,
        },
        status=status.HTTP_201_CREATED
    )
