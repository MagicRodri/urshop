
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from products.models import Product

from .models import Cart, CartItem

# Create your views here.


def cart_add(request:HttpRequest,product_slug : str):

    product = get_object_or_404(Product,slug=product_slug)

    cart , _= Cart.objects.get_or_new(request)

    item , created = CartItem.objects.get_or_create(cart=cart,product=product)
    if not created:
        item.increment()
        return redirect(reverse('products:list'))

    return redirect(reverse('products:list'))


def cart_detail(request):

    cart , _ = Cart.objects.get_or_new(request)

    context = {
        'cart' : cart,
        'items' : cart.items.all()
    }
    return render(request,'carts/cart_detail.html',context=context)