from django.db.models.signals import pre_save

from .models import Order

def order_pre_save(instance,sender,*args, **kwargs):

    pass


pre_save.connect(order_pre_save,sender = Order)