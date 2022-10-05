import random

from django.http import HttpRequest

SESSION_CART_ID_KEY = 'cart_id'

def get_cart_id(request : HttpRequest = None) -> str:
    if not request.session.get(SESSION_CART_ID_KEY):

        request.session[SESSION_CART_ID_KEY] = generate_cart_id()

    return request.session[SESSION_CART_ID_KEY]

def generate_cart_id(k:int = 50) -> str:

    a ='ABCDEFGHIJKLMNOPQRQSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&-+=_*()'

    return ''.join(random.choices(a,k=k))
