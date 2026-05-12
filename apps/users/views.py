"""
Users App — API Views (Layer 5)

Each view:
1. Validates input via serializer
2. Checks business rules (Layer 6)
3. Calls business logic (Layer 7)
4. Returns formatted response

Views never touch the database directly.
"""
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model, login as django_login
from django.core.exceptions import ValidationError

from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserProfileSerializer,
    ForgotPasswordSerializer,
    ResetPasswordSerializer,
    VerifyEmailSerializer,
)
from .business_rules import (
    validate_password_strength,
    validate_role,
    validate_name_not_empty,
)
from .business_logic import (
    create_user,
    generate_verification_token,
    send_verification_email,
    verify_email_token,
    generate_password_reset_token,
    send_password_reset_email,
    reset_password_with_token,
)

User = get_user_model()


@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    """
    POST /api/v1/auth/register/

    Creates a new user account and sends verification email.
    User cannot log in until email is verified.
    """
    serializer = RegisterSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            {'errors': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    data = serializer.validated_data

    # Layer 6 — Business Rules
    try:
        validate_password_strength(data['password'])
        validate_role(data['role'])
        validate_name_not_empty(data['first_name'], data['last_name'])
    except ValidationError as e:
        return Response(
            {'errors': {'detail': str(e.message)}},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Layer 7 — Business Logic
    user = create_user(
        email=data['email'],
        password=data['password'],
        role=data['role'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        phone_number=data.get('phone_number', ''),
    )

    # Send verification email
    raw_token = generate_verification_token(user)
    try:
        send_verification_email(user, raw_token)
    except Exception:
        # Email failure should not block registration
        pass

    return Response(
        {
            'message': 'Account created. Please check your email to verify your account.',
            'user': UserProfileSerializer(user).data,
        },
        status=status.HTTP_201_CREATED
    )


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """
    POST /api/v1/auth/login/

    Authenticates user and returns JWT tokens.
    Also establishes Django session for template-based views.
    Returns access token (stored in JS memory) + refresh token.
    Routes user to landlord or tenant dashboard based on role.
    """
    serializer = LoginSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            {'errors': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    email = serializer.validated_data['email'].lower().strip()
    password = serializer.validated_data['password']

    # Fetch user — generic error to prevent user enumeration
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response(
            {'errors': {'detail': 'Invalid email or password.'}},
            status=status.HTTP_401_UNAUTHORIZED
        )

    # Check password
    if not user.check_password(password):
        return Response(
            {'errors': {'detail': 'Invalid email or password.'}},
            status=status.HTTP_401_UNAUTHORIZED
        )

    # Check if email is verified
    if not user.is_verified:
        return Response(
            {'errors': {'detail': 'Please verify your email before logging in.'}},
            status=status.HTTP_403_FORBIDDEN
        )

    # Check if account is active (not soft-deleted)
    if not user.is_active:
        return Response(
            {'errors': {'detail': 'This account has been deactivated.'}},
            status=status.HTTP_403_FORBIDDEN
        )

    # Generate JWT tokens
    refresh = RefreshToken.for_user(user)

    # Establish Django session for template-based views
    # This allows request.user.is_authenticated to work in Django views
    django_login(request, user)

    # Determine dashboard redirect based on role
    redirect_url = '/landlord/dashboard/' if user.role == 'landlord' else '/tenant/dashboard/'

    return Response({
        'access': str(refresh.access_token),
        'refresh': str(refresh),
        'user': UserProfileSerializer(user).data,
        'redirect': redirect_url,
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def verify_email_view(request):
    """
    POST /api/v1/auth/verify-email/

    Verifies email using the token sent during registration.
    """
    serializer = VerifyEmailSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            {'errors': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = verify_email_token(serializer.validated_data['token'])

    if not user:
        return Response(
            {'errors': {'detail': 'Invalid or expired verification link.'}},
            status=status.HTTP_400_BAD_REQUEST
        )

    return Response({'message': 'Email verified successfully. You can now log in.'})


@api_view(['POST'])
@permission_classes([AllowAny])
def forgot_password_view(request):
    """
    POST /api/v1/auth/forgot-password/

    Sends password reset email. Always returns 200 to prevent
    user enumeration — even if the email doesn't exist.
    """
    serializer = ForgotPasswordSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            {'errors': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    email = serializer.validated_data['email'].lower().strip()

    # Always return success — never reveal if email exists
    try:
        user = User.objects.get(email=email)
        raw_token = generate_password_reset_token(user)
        send_password_reset_email(user, raw_token)
    except User.DoesNotExist:
        pass  # Silent — prevents user enumeration
    except Exception:
        pass  # Email failure should not expose information

    return Response({
        'message': 'If an account with that email exists, a reset link has been sent.'
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def reset_password_view(request):
    """
    POST /api/v1/auth/reset-password/

    Resets password using the token from the reset email.
    Token expires after 15 minutes.
    """
    serializer = ResetPasswordSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            {'errors': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    data = serializer.validated_data

    # Validate new password strength
    try:
        validate_password_strength(data['new_password'])
    except ValidationError as e:
        return Response(
            {'errors': {'detail': str(e.message)}},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = reset_password_with_token(data['token'], data['new_password'])

    if not user:
        return Response(
            {'errors': {'detail': 'Invalid or expired reset link.'}},
            status=status.HTTP_400_BAD_REQUEST
        )

    return Response({'message': 'Password reset successfully. You can now log in.'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me_view(request):
    """
    GET /api/v1/auth/me/

    Returns the currently authenticated user's profile.
    Used by the frontend to check auth state and get user data.
    """
    return Response(UserProfileSerializer(request.user).data)
