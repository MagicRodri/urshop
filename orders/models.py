
from django.db import models
from django.contrib.auth import get_user_model

from core.models import TimeStampedModel
from carts.models import Cart
# Create your models here.
User = get_user_model()

class Address(TimeStampedModel):


    BILLING = 'BILLING'
    SHIPPING = 'SHIPPING'

    ADDRESS_TYPES = (
    (BILLING, 'Billing address'),
    (SHIPPING, 'Shipping address'),
    )

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 128, blank = True)
    address_type = models.CharField(max_length = 16, default = BILLING, choices = ADDRESS_TYPES)
    address_line_1 = models.CharField(max_length = 128)
    address_line_2 = models.CharField(max_length = 128, blank = True)
    country = models.CharField(max_length = 128)
    state = models.CharField(max_length = 128,blank = True)
    city = models.CharField(max_length = 128)
    postal_code = models.CharField(max_length = 128)

    class Meta:
        verbose_name_plural = 'Addresses'


class Order(TimeStampedModel):

    CREATED = 'CREATED'
    PAID = 'PAID'
    SHIPPED = 'SHIPPED'
    CANCELED = 'CANCELED' 

    ORDER_STATUS = (
        (CREATED, 'Created'),
        (PAID, 'Paid'),
        (SHIPPED, 'Shipped'),
        (CANCELED, 'Canceled'),
    )
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    order_id = models.CharField(max_length = 128, blank = True)
    address = models.ForeignKey(Address, on_delete = models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    shipping_total = models.DecimalField(default = 0.00, decimal_places = 2, max_digits = 10)
    total = models.DecimalField(default = 0.00, decimal_places = 2, max_digits = 10)
    # payment_type = models.CharField(max_lenght = 16,)
    status = models.CharField(max_length = 16, default = CREATED ,choices = ORDER_STATUS)
    active = models.BooleanField(default = True)