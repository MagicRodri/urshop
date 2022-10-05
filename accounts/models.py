from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    picture = models.ImageField(upload_to = 'users/',blank = True, null = True)


    def __str__(self) -> str:
        return self.username