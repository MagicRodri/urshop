from email.policy import default

from django.db import models

from core.models import BaseModel
from orders.models import Order

# Create your models here.

class Payment(BaseModel):
    order = models.ForeignKey(Order,on_delete = models.CASCADE)
    method = models.CharField(max_length = 64)
    successful = models.BooleanField(default = False)