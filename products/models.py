
from django.db import models

from core.models import TimeStampedModel
# Create your models here.

class Product(TimeStampedModel):
    name = models.CharField(max_length=164)
    description = models.TextField()
    price = models.FloatField()
