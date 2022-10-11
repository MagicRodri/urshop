
from django.db import models 
from django.db.models.functions import Coalesce
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.http import HttpRequest

from products.models import Product
from core.models import TimeStampedModel
from core.utils import get_user_id
# Create your models here.

User = get_user_model()

    
class CartManager(models.Manager):

    
    def get_or_new(self,request : HttpRequest = None):

        """
            Get or create a new cart object based on request
        """

        if request.user.is_authenticated:
            return self.model.objects.get_or_create(customer = request.user)
        else:
            return self.model.objects.get_or_create(cart_id = get_user_id(request))

class Cart(TimeStampedModel):


    cart_id = models.CharField(max_length=128,blank = True)
    customer = models.OneToOneField(User,blank=True,null = True,on_delete = models.CASCADE)

    objects = CartManager()
    def __str__(self) -> str:
        if self.customer:
            return str(self.customer)
        return self.cart_id    

    @property
    def total(self) -> float:
        total = self.items.all().aggregate(total = Coalesce(models.Sum('product__price'),0.0,output_field=models.FloatField())) # a dict
        return total['total']

class CartItem(TimeStampedModel):

    cart = models.ForeignKey(Cart,related_name = 'items',on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)

    @property
    def name(self) -> str:
        return self.product.name

    @property
    def price(self) -> float:
        return float(self.product.price)

    @property
    def total(self) -> float:
        return self.quantity * self.price

    def _validate_item_quantity(self):
        """
            Raises a validation error if quantity is more than product quantity
        """
        prod_quantity = self.product.quantity
        quantity = self.quantity
        if quantity > prod_quantity:
            raise ValidationError(f'Item quantity ({quantity}) can not be more than available product quantity({prod_quantity})')
    
    def save(self,*args, **kwargs):
        self._validate_item_quantity()
        return super().save(*args, **kwargs)