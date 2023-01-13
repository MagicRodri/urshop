from email.policy import default

from django.db import models

from core.models import BaseModel
from orders.models import Order

# Create your models here.


class PaymentBaseModel(BaseModel):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    method = models.CharField(max_length=50)

    class Meta:
        abstract = True


class StripePayment(PaymentBaseModel):

    amount_total = models.PositiveIntegerField()
    currency = models.CharField(max_length=10, blank=True)
    stripe_charge_id = models.CharField(max_length=100)
    intent_id = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Stripe Payment'
        verbose_name_plural = 'Stripe Payments'

    def __repr__(self) -> str:
        return f'<Stripe Payment {self.intent_id}>'