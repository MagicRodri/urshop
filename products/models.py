
from wsgiref.validate import validator
from django.urls import reverse
from django.db import models

from .utils import product_quantity_validator

from core.models import TimeStampedModel
# Create your models here.

class Category(TimeStampedModel):
    name = models.CharField(max_length=128,unique=True)
    slug = models.SlugField(max_length=128,blank=True,unique=True,null=True)
    description = models.TextField(blank = True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:

        return self.name

class Brand(TimeStampedModel):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

    

class Product(TimeStampedModel):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128,blank=True,unique=True,null=True)
    brand = models.ForeignKey(Brand,blank=True,null=True,on_delete=models.SET_NULL,related_name = 'products')
    category = models.ManyToManyField(Category)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=15,default=9.99)
    old_price = models.DecimalField(decimal_places=2,max_digits=15,default=0, blank=True)
    quantity = models.IntegerField(default=1,validators = [product_quantity_validator])
    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})
    

class Image(TimeStampedModel):
    title = models.CharField(max_length=128,blank=True)
    image = models.ImageField(upload_to = 'products/')
    product = models.ForeignKey(Product,related_name='images',on_delete=models.CASCADE)

    def __str__(self) -> str:
        if self.title :
            return self.title
        return super().__str__()
