from django.urls import path

from .views import (
    create_checkout_session,
    payments_success,
    payments_cancel,
    stripe_webhook
)

app_name = 'payments'
urlpatterns = [
    path('cancel/',payments_cancel,name='cancel'),
    path('checkout/<int:pk>/',create_checkout_session,name='create-checkout-session'),
    path('success/',payments_success,name='success'),
    path('webhooks/stripe/',stripe_webhook,name='stripe-webhook'),
]