"""
Users App — URL Configuration

All auth endpoints under /api/v1/auth/
"""
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

app_name = 'users'

urlpatterns = [
    # Registration
    path('register/', views.register_view, name='register'),

    # Login (JWT issue)
    path('login/', views.login_view, name='login'),

    # Token refresh
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Email verification
    path('verify-email/', views.verify_email_view, name='verify_email'),

    # Password reset flow
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('reset-password/', views.reset_password_view, name='reset_password'),

    # Current user profile
    path('me/', views.me_view, name='me'),
]
