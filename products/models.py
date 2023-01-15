from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.urls import reverse

from core.models import BaseModel
from core.utils import delete_file, reverse_querystring, thumbnail_image

# Create your models here.

User = get_user_model()


class Category(BaseModel):
    name = models.CharField(max_length=128, unique=True)
    image = models.ImageField(upload_to='categories/originals/', blank=True)
    thumbnail = models.ImageField(upload_to='categories/thumbnails/',
                                  blank=True)
    slug = models.SlugField(max_length=128, blank=True, unique=True, null=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self) -> str:
        return self.name

    # def get_absolute_url(self):
    #     return reverse_querystring("products:list",query_kwargs={'category': self.slug})
    

    def save(self, *args, **kwargs):
        # if self.image:
        #     thumbnail_image(self)
        # qs = Category.objects.filter(name__iexact = self.name ).exclude(pk = self.pk)
        # if qs.exists():
        #     return qs.first()
        super().save(*args, **kwargs)



class Brand(BaseModel):
    name = models.CharField('brand-name', max_length=128)

    def save(self, *args, **kwargs):
        # qs = Brand.objects.filter(name__iexact = self.name )
        # if qs.exists():
        #     return qs.first()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Product(BaseModel):
    user = models.ForeignKey(User,
                             related_name='products',
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, blank=True, unique=True, null=True)
    brand = models.ForeignKey(Brand,
                              blank=True,
                              null=True,
                              on_delete=models.SET_NULL,
                              related_name='products')
    categories = models.ManyToManyField(Category, related_name='products')
    description = models.TextField(default='Description here!')
    price = models.DecimalField(decimal_places=2, max_digits=15, default=9.99)
    old_price = models.DecimalField(decimal_places=2,
                                    max_digits=15,
                                    default=0,
                                    blank=True)
    quantity = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(0, message='Quantity must be greater than 0'),
        ])

    def __str__(self) -> str:
        return self.name
    
    def preview(self):
        return self.images.first().image.url

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})


class Image(BaseModel):
    title = models.CharField(max_length=128, blank=True)
    image = models.ImageField(upload_to='products/originals/')
    thumbnail = models.ImageField(upload_to='products/thumbnails/', blank=True)
    product = models.ForeignKey(Product,
                                related_name='images',
                                on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.product.name

def image_pre_save(instance, sender, *args, **kwargs):
    ...
    # thumbnail_image(instance)


pre_save.connect(image_pre_save, sender=Image)


def image_pre_delete(instance, sender, *args, **kwargs):
    ...
    # delete_file(instance.image.path)
    # if instance.thumbnail:
    #     delete_file(instance.thumbnail.path)


pre_delete.connect(image_pre_delete, sender=Image)
