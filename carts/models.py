
from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product
from products.utils import product_quantity_validator
from core.models import TimeStampedModel
# Create your models here.

User = get_user_model()

    


class Cart(TimeStampedModel):

    cart_id = models.CharField(max_length=128,blank = True)
    customer = models.OneToOneField(User,blank=True,null = True,on_delete = models.CASCADE)
    
    @property
    def total(self) -> float:
        total = 0
        for item in self.items.all():
            total += item.total
        return total

class CartItem(TimeStampedModel):

    cart = models.ForeignKey(Cart,related_name = 'items',on_delete = models.CASCADE)
    customer = models.ForeignKey(User,blank=True,null = True,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1,validators = [product_quantity_validator])

    @property
    def name(self) -> str:
        return self.product.name

    @property
    def price(self) -> float:
        return float(self.product.price)

    @property
    def total(self) -> float:
        return self.quantity * self.price