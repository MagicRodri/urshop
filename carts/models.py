
from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from products.models import Product
from core.models import TimeStampedModel

# Create your models here.

User = get_user_model()

    


class Cart(TimeStampedModel):

    cart_id = models.CharField(max_length=128,blank = True)
    customer = models.OneToOneField(User,blank=True,null = True,on_delete = models.CASCADE)

    def __str__(self) -> str:
        if self.customer:
            return str(self.customer)
        return self.cart_id    

    @property
    def total(self) -> float:
        total = 0
        for item in self.items.all():
            total += item.total
        return total

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