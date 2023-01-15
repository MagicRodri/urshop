
from django.db import models
from django.db.models.signals import post_save
from PIL import Image

from core.models import BaseModel
from core.utils import resize_image
from orders.models import Order

# Create your models here.

class Currency(BaseModel):

    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    symbol = models.CharField(max_length=10)
    image = models.ImageField(upload_to='currencies/', blank=True)

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self) -> str:
        return f'<Currency {self.name}>'

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

def currency_post_save(sender, instance, *args, **kwargs):
    if instance.image:
        image = Image.open(instance.image)
        image = resize_image(image,(25,15))
        image.save(instance.image.path)
        
post_save.connect(currency_post_save, sender=Currency)