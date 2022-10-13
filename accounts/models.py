
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    picture = models.ImageField(upload_to = 'users/',blank = True, null = True)


    def __str__(self) -> str:
        return self.username


def user_pre_save(instance,sender,*args, **kwargs):
    ...