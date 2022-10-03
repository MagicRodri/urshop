from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver

from .models import Product,Category

from core.utils import slugify_instance_name

def pre_slugify_save(instance,sender,*args, **kwargs):
    """
        Check if instance has slug and assign new otherwise
    """
    if not instance.slug:
        slugify_instance_name(instance=instance)

pre_save.connect(pre_slugify_save,sender=Product)
pre_save.connect(pre_slugify_save,sender=Category)

def post_slugify_save(instance,sender,created,*args, **kwargs):
    """
        Check if created instance's slug doesn't exist yet and add modify if so
    """
    if created:
        slugify_instance_name(instance=instance,new_slug=instance.slug,save=True)

post_save.connect(post_slugify_save,sender=Product)
post_save.connect(post_slugify_save,sender=Category)