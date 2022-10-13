import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.http import HttpRequest

from carts.models import Cart
from core.models import BaseModel
from core.utils import get_user_id

# Create your models here.
User = get_user_model()

class Address(BaseModel):


    BILLING = 'BILLING'
    SHIPPING = 'SHIPPING'

    ADDRESS_TYPES = (
    (BILLING, 'Billing address'),
    (SHIPPING, 'Shipping address'),
    )

    user = models.ForeignKey(User, on_delete = models.CASCADE , blank = True , null = True)
    name = models.CharField(max_length = 128, blank = True)
    address_type = models.CharField(max_length = 16, default = BILLING, choices = ADDRESS_TYPES)
    address_line_1 = models.CharField(max_length = 128)
    address_line_2 = models.CharField(max_length = 128, blank = True)
    country = models.CharField(max_length = 128)
    state = models.CharField(max_length = 128,blank = True)
    city = models.CharField(max_length = 128)
    zip = models.CharField(max_length = 128)

    class Meta:
        verbose_name_plural = 'Addresses'

class OrderManager(models.Manager):

    def get_or_new(self,request : HttpRequest = None):

        """
            Get or create a new order object based on request
        """

        if request.user.is_authenticated:
            return self.model.objects.get_or_create(user = request.user)
        else:
            return self.model.objects.get_or_create(cart_id = get_user_id(request))

class Order(BaseModel):

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
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True , null = True )
    order_id = models.CharField(max_length = 128, blank = True)
    address = models.ForeignKey(Address, on_delete = models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    shipping_total = models.DecimalField(default = 0.00, decimal_places = 2, max_digits = 10)
    # payment_type = models.CharField(max_lenght = 16,)
    status = models.CharField(max_length = 16, default = CREATED ,choices = ORDER_STATUS)

    objects = OrderManager()