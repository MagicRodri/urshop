from django.db import models

from core.models import TimeStampedModel
# Create your models here.

class Address(TimeStampedModel):
    user = models.ForeignKey