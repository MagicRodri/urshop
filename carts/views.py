
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from products.models import Product

from .models import Cart, CartItem


def cart_add(request:HttpRequest,product_slug : str):

    product = get_object_or_404(Product,slug=product_slug)

    cart , _= Cart.objects.get_or_new(request)

    item , created = CartItem.objects.get_or_create(cart=cart,product=product)
    if not created:
        item.increment()

    return redirect(reverse('carts:detail'))

def cart_decrement(request:HttpRequest,product_slug : str):

    product = get_object_or_404(Product,slug=product_slug)

    cart , _= Cart.objects.get_or_new(request)

    item , created = CartItem.objects.get_or_create(cart=cart,product=product)
    if not created:
        item.decrement()

    return redirect(reverse('carts:detail'))

def cart_remove(request:HttpRequest,item_pk : int):
    item = get_object_or_404(CartItem, pk=item_pk)
    item.delete()
    return redirect(reverse('carts:detail'))

def cart_detail(request):
    return render(request,'carts/cart_detail.html')