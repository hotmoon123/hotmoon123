"""
Users App — Business Rules (Layer 6)

Fixed, non-negotiable system constraints for user operations.
These are checked BEFORE business logic executes.
"""
import re
from django.core.exceptions import ValidationError


def validate_email_format(email):
    """Validate email format using regex pattern."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise ValidationError('Invalid email format.')


def validate_password_strength(password):
    """
    Password must be at least 8 characters with:
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    """
    if len(password) < 8:
        raise ValidationError('Password must be at least 8 characters.')
    if not re.search(r'[A-Z]', password):
        raise ValidationError('Password must contain at least one uppercase letter.')
    if not re.search(r'[a-z]', password):
        raise ValidationError('Password must contain at least one lowercase letter.')
    if not re.search(r'[0-9]', password):
        raise ValidationError('Password must contain at least one digit.')


def validate_role(role):
    """Role must be exactly 'landlord' or 'tenant'."""
    if role not in ('landlord', 'tenant'):
        raise ValidationError('Role must be either landlord or tenant.')


def validate_name_not_empty(first_name, last_name):
    """First and last name are required and must not be blank."""
    if not first_name or not first_name.strip():
        raise ValidationError('First name is required.')
    if not last_name or not last_name.strip():
        raise ValidationError('Last name is required.')
