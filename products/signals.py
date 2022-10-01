from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver

from .models import Product

from core.utils import slugify_instance_name

@receiver(pre_save,sender=Product)
def pre_product_save(instance,sender,*args, **kwargs):
    """
        Check if instance has slug and assign new otherwise
    """
    if not instance.slug:
        slugify_instance_name(instance=instance)


@receiver(post_save,sender=Product)
def post_product_save(instance,sender,created,*args, **kwargs):
    """
        Check if created instance's slug doesn't exist yet and add modify if so
    """
    if created:
        slugify_instance_name(instance=instance,new_slug=instance.slug,save=True)