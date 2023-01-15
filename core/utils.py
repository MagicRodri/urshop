import os
import random

from django.conf import settings
from django.http import HttpRequest
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.text import slugify
from PIL import Image

SESSION_USER_ID_KEY = 'urshop_anonymous_user_id'


def slugify_instance_name(instance,save=False,new_slug=None):
    """
        slugify instance's name and assign it to instance.slug
        instance must have both name and slug fields
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)
    Klass = instance.__class__    
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists() :
        rand_int= random.randint(1,400_000)
        slug = f"{slug}-{rand_int}"
        return slugify_instance_name(instance,save=save,new_slug=slug)
    instance.slug = slug
    if save : 
        instance.save()
    return instance


def get_user_id(request : HttpRequest = None) -> str:
    
    """
        Function to retrieve a user's session id
    """
    if not request.session.get(SESSION_USER_ID_KEY):

        request.session[SESSION_USER_ID_KEY] = generate_id()

    return request.session[SESSION_USER_ID_KEY]

def generate_id(k:int = 50) -> str:
    """
        Generate a random id of length of k
        Default k=50 
    """

    a ='ABCDEFGHIJKLMNOPQRQSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&-+=_*()'

    return ''.join(random.choices(a,k=k))


def thumbnail_image(instance) -> None:
    """
        Create a thumbnail of the given instance's image and save it in the thumbails directory path
        Instance must have both image and thumbnail fields as models.ImageField
    """

    IMG_MAX_SIZE = (800,800)
    
    thumbnail_absolute_path = settings.MEDIA_ROOT / instance.thumbnail.field.upload_to
    original_image_name = os.path.basename(instance.image.path)

    # Check if thumbnails directory exists, otherwise create
    if not thumbnail_absolute_path.exists():
        os.makedirs(thumbnail_absolute_path)

    # Resize originale image    
    image = Image.open(instance.image)
    image.thumbnail(IMG_MAX_SIZE)

    # Thumbnail name as thumbnail_<original name>
    thumbnail_name = f'thumbnail_{original_image_name}'
    thumbnail_path = thumbnail_absolute_path / thumbnail_name

    with open(thumbnail_path,'w'):
        # Save resized image under thumbnail's path
        image.save(thumbnail_path)
        # Assign resized image to instance's thumbnail
        instance.thumbnail = os.path.join(instance.thumbnail.field.upload_to , thumbnail_name)

def delete_file(path):
    """ 
        Delete the file of the given path and return True otherwise False
    """

    if os.path.isfile(path):
        os.remove(path)
        return True

    return False


def reverse_querystring(*args, query_kwargs=None, **kwargs):
    """
    Reverse a URL with query string parameters.
    """
    url = reverse(*args, **kwargs)
    if query_kwargs:
        querystring = urlencode(query_kwargs)
        url = f"{url}?{querystring}"
    return url

def resize_image(image, size=(800,800)):
    """
        Resize the given image to the given size
    """
    image.thumbnail(size)
    return image