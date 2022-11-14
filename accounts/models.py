
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save

from core.utils import thumbnail_image

# Create your models here.

class User(AbstractUser):

    SHOPPER = 'SHOPPER'
    SELLER = 'SELLER'

    USER_TYPE = (
        (SHOPPER, 'Shopper'),
        (SELLER, 'Seller'),
    )
    picture = models.ImageField(upload_to = 'users/',blank = True)
    type = models.CharField(max_length = 16 ,choices = USER_TYPE, default = SHOPPER)


    def __str__(self) -> str:
        return self.username


def user_pre_save(instance,sender,*args, **kwargs):
    ...

pre_save.connect(user_pre_save,sender = User)