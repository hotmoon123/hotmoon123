"""
Users App — Business Logic (Layer 7)

Dynamic process orchestration for user operations.
Calls Data Retrieval (Layer 8) and Data Storage (Layer 9) — never touches DB directly.
"""
import hashlib
import secrets
from datetime import timedelta

from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


def create_user(email, password, role, first_name, last_name, phone_number=''):
    """
    Create a new user account.
    Password is hashed automatically by Django's set_password (bcrypt).
    User starts as unverified — must verify email before login.
    """
    user = User.objects.create_user(
        email=email.lower().strip(),
        password=password,
        role=role,
        first_name=first_name.strip(),
        last_name=last_name.strip(),
        phone_number=phone_number.strip() if phone_number else '',
        is_verified=False,
    )
    return user


def generate_verification_token(user):
    """
    Generate a secure email verification token.
    Token is stored as a hash — the raw token is sent via email and never stored.
    Returns the raw token (to be emailed) — only the hash is saved.
    """
    raw_token = secrets.token_urlsafe(48)
    token_hash = hashlib.sha256(raw_token.encode()).hexdigest()

    # Store token hash and expiry on the user (using cache or a dedicated table)
    # For now, we use Django's cache framework for simplicity
    from django.core.cache import cache
    cache.set(
        f'email_verify_{token_hash}',
        {'user_id': user.id, 'created_at': timezone.now().isoformat()},
        timeout=86400  # 24 hours
    )
    return raw_token


from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

def send_verification_email(user, raw_token):
    """Send beautiful HTML 'Sweet Welcome' email verification link."""
    verify_url = f"http://{settings.ALLOWED_HOSTS[0]}:8000/verify-email?token={raw_token}"
    
    # Render the sweet HTML template
    html_content = render_to_string('emails/welcome_email.html', {
        'user': user,
        'verify_url': verify_url
    })
    text_content = strip_tags(html_content) # Fallback for email clients that don't support HTML

    email = EmailMultiAlternatives(
        subject="You are welcome to RentFlow! 🏠",
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@rentflow.com',
        to=[user.email]
    )
    email.attach_alternative(html_content, "text/html")
    
    try:
        email.send(fail_silently=False)
    except Exception as e:
        print(f"Error sending email: {e}")



def verify_email_token(raw_token):
    """
    Verify email token and activate user account.
    Returns the user if successful, None if token is invalid/expired.
    """
    from django.core.cache import cache

    token_hash = hashlib.sha256(raw_token.encode()).hexdigest()
    data = cache.get(f'email_verify_{token_hash}')

    if not data:
        return None

    try:
        user = User.objects.get(id=data['user_id'])
        user.is_verified = True
        user.save(update_fields=['is_verified', 'updated_at'])

        # Delete the used token
        cache.delete(f'email_verify_{token_hash}')
        return user
    except User.DoesNotExist:
        return None


def generate_password_reset_token(user):
    """
    Generate a password reset token with 15-minute expiry.
    Returns the raw token to be emailed.
    """
    raw_token = secrets.token_urlsafe(48)
    token_hash = hashlib.sha256(raw_token.encode()).hexdigest()

    from django.core.cache import cache
    cache.set(
        f'password_reset_{token_hash}',
        {'user_id': user.id, 'created_at': timezone.now().isoformat()},
        timeout=900  # 15 minutes
    )
    return raw_token


def send_password_reset_email(user, raw_token):
    """Send password reset link to the user."""
    reset_url = f'{settings.ALLOWED_HOSTS[0]}:8000/reset-password?token={raw_token}'

    send_mail(
        subject='Reset your password — Rent & Lease Management',
        message=(
            f'Hi {user.first_name},\n\n'
            f'Click the link below to reset your password:\n'
            f'{reset_url}\n\n'
            f'This link expires in 15 minutes.\n'
            f'If you did not request this, ignore this email.\n\n'
            f'— Rent & Lease Management System'
        ),
        from_email='noreply@rentlease.com',
        recipient_list=[user.email],
        fail_silently=False,
    )


def reset_password_with_token(raw_token, new_password):
    """
    Reset password using a valid token.
    Returns the user if successful, None if token is invalid/expired.
    """
    from django.core.cache import cache

    token_hash = hashlib.sha256(raw_token.encode()).hexdigest()
    data = cache.get(f'password_reset_{token_hash}')

    if not data:
        return None

    try:
        user = User.objects.get(id=data['user_id'])
        user.set_password(new_password)
        user.save(update_fields=['password', 'updated_at'])

        # Delete the used token
        cache.delete(f'password_reset_{token_hash}')
        return user
    except User.DoesNotExist:
        return None
