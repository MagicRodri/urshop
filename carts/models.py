
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.functions import Coalesce
from django.db.models.signals import post_save, pre_save
from django.http import HttpRequest

from core.models import BaseModel
from core.utils import get_user_id
from products.models import Product

# Create your models here.

User = get_user_model()
    

class CartQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active = True)
    
class CartManager(models.Manager):

    def get_queryset(self):
        return CartQuerySet(model=self.model,using=self.db)
    
    def get_or_new(self,request : HttpRequest = None):

        """
            Get or create a new cart object based on request
        """

        if request.user.is_authenticated:
            return self.get_queryset().active().get_or_create(user = request.user)
        else:
            return self.get_queryset().active().get_or_create(cart_id = get_user_id(request))

class Cart(BaseModel):


    cart_id = models.CharField(max_length=128,blank = True)
    user = models.ForeignKey(User,blank=True,null = True,on_delete = models.CASCADE)

    objects = CartManager()
    def __str__(self) -> str:
        if self.user:
            return str(self.user)
        return self.cart_id    

    @property
    def total(self) -> float:
        total = self.items.all().aggregate(total = Coalesce(models.Sum('product__price'),0.0,output_field=models.FloatField())) # a dict
        return total['total']

class CartItem(BaseModel):

    cart = models.ForeignKey(Cart,related_name = 'items',on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)


    def increment(self,n=1):
        self.quantity += n
        self.save()

    def increment(self,n=1):
        self.quantity -= n
        self.save()

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


def cart_item_pre_save(instance,sender,*args, **kwargs):
    qs = CartItem.objects.filter(cart = instance.cart, product=instance.product).exclude(id = instance.id)
    print('pre:',qs.count())
    if qs.count() == 1:
        existing_item = qs.first()
        existing_item.increment(instance.quantity)

pre_save.connect(cart_item_pre_save,sender = CartItem)


def cart_item_post_save(instance, sender,created,*args, **kwargs):

    qs = CartItem.objects.filter(cart = instance.cart,product=instance.product).exclude(id = instance.id)
    print('post:',qs.count())
    if qs.count() == 1:
        instance.delete()
post_save.connect(cart_item_post_save, sender = CartItem) 