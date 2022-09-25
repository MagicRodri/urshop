

from django.db import models

from core.models import TimeStampedModel
# Create your models here.

class ProductCategory(TimeStampedModel):
    name = models.CharField(max_length=164)

class Product(TimeStampedModel):
    name = models.CharField(max_length=164)
    slug = models.SlugField(blank=True,unique=True,null=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=15,default=9.99)
    category = models.ManyToManyField(ProductCategory)

class ProductImage(TimeStampedModel):
    title = models.CharField(max_length=164,blank=True)
    image = models.ImageField(upload_to = 'products/')
    product = models.ForeignKey(Product,related_name='images',on_delete=models.CASCADE)
