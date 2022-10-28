import random

from django.http import HttpRequest
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


def thumbnail_image(image_field) -> None:
    """
        Create a thumbnail of the given image field's image and save it under the original image's path
    """
    IMG_MAX_SIZE = (800,800)
    image = Image.open(image_field)
    image.thumbnail(IMG_MAX_SIZE)
    image.save(image_field.path)