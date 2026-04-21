"""
Custom exceptions for the Rent & Lease Management System.
"""


class BusinessRuleError(Exception):
    """Raised when a business rule validation fails."""
    pass


class EmailServiceError(Exception):
    """Raised when email sending fails."""
    pass


class PaymentError(Exception):
    """Raised when payment processing fails."""
    pass


class AuthorizationError(Exception):
    """Raised when user is not authorized to perform an action."""
    pass


class ResourceNotFoundError(Exception):
    """Raised when a requested resource is not found."""
    pass


class ValidationError(Exception):
    """Raised when data validation fails."""
    pass
