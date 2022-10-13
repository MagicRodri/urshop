
from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    is_active = models.BooleanField(default = True)
    
    class Meta:
        abstract = True
        ordering = ['-created']