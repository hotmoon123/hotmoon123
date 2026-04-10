"""
Financials App — URL Configuration

All financial endpoints under /api/v1/financials/
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = "financials"

router = DefaultRouter()
router.register(r"invoices", views.InvoiceViewSet, basename="invoice")
router.register(r"transactions", views.TransactionViewSet, basename="transaction")
router.register(r"expenses", views.ExpenseViewSet, basename="expense")
router.register(
    r"payment-methods", views.PaymentMethodViewSet, basename="payment-method"
)

urlpatterns = [
    path("", include(router.urls)),
]
