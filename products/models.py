

from django.db import models

from core.models import TimeStampedModel
# Create your models here.

class Category(TimeStampedModel):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128,blank=True,unique=True,null=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Categories'

class Brand(TimeStampedModel):
    name = models.CharField(max_length=64)

    

class Product(TimeStampedModel):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128,blank=True,unique=True,null=True)
    brand = models.ForeignKey(Brand,blank=True,null=True,related_name='products',on_delete=models.SET_NULL)
    category = models.ManyToManyField(Category)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=15,default=9.99)
    old_price = models.DecimalField(decimal_places=2,max_digits=15,default=0, blank=True)
    quantity = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    

class Image(TimeStampedModel):
    title = models.CharField(max_length=128,blank=True)
    image = models.ImageField(upload_to = 'products/')
    product = models.ForeignKey(Product,related_name='images',on_delete=models.CASCADE)
