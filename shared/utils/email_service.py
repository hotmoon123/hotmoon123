"""
Shared email service for the Rent & Lease Management System.
Handles all email sending with proper error handling and logging.
"""
import logging
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from shared.exceptions import EmailServiceError

logger = logging.getLogger(__name__)


def send_email(subject, recipient_list, template_name=None, context=None, 
               text_content=None, html_content=None, fail_silently=False):
    """
    Send an email with HTML and text fallback.
    
    Args:
        subject: Email subject line
        recipient_list: List of recipient email addresses
        template_name: Path to HTML template (optional)
        context: Template context (optional)
        text_content: Plain text content (optional, auto-generated if template used)
        html_content: HTML content (optional, rendered from template if provided)
        fail_silently: Whether to suppress exceptions
    
    Returns:
        bool: True if email sent successfully, False otherwise
    
    Raises:
        EmailServiceError: If email sending fails and fail_silently is False
    """
    try:
        # Render HTML from template if provided
        if template_name and context:
            html_content = render_to_string(template_name, context)
            if not text_content:
                text_content = strip_tags(html_content)
        
        if not html_content and not text_content:
            raise EmailServiceError("Either html_content or text_content must be provided")
        
        from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@rentflow.com')
        
        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content or '',
            from_email=from_email,
            to=recipient_list,
        )
        
        if html_content:
            email.attach_alternative(html_content, "text/html")
        
        email.send(fail_silently=fail_silently)
        logger.info(f"Email sent successfully to {recipient_list}")
        return True
        
    except EmailServiceError:
        if not fail_silently:
            raise
        logger.error(f"Email service error: {subject} to {recipient_list}")
        return False
    except Exception as e:
        logger.error(f"Unexpected email error: {e}")
        if not fail_silently:
            raise EmailServiceError(f"Failed to send email: {str(e)}") from e
        return False


def send_templated_email(subject, recipient_list, template_name, context, fail_silently=False):
    """
    Convenience method for sending templated emails.
    
    Args:
        subject: Email subject
        recipient_list: List of recipients
        template_name: Template path (e.g., 'emails/welcome_email.html')
        context: Template context dict
        fail_silently: Whether to suppress exceptions
    
    Returns:
        bool: Success status
    """
    return send_email(
        subject=subject,
        recipient_list=recipient_list,
        template_name=template_name,
        context=context,
        fail_silently=fail_silently,
    )
