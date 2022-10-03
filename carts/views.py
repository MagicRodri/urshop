from django.shortcuts import render,get_object_or_404
from django.http import HttpRequest

from products.models import Product
from .models import CartItem,Cart
# Create your views here.


def cart_add(request:HttpRequest,product_slug : str):
    product = get_object_or_404(Product,slug=product_slug)

    cart , created = Cart.objects.get_or_create(customer = request.user)
    item = CartItem.objects.create(product=product)

    return render(request,'cart_add.html')