
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpRequest
from django.urls import reverse

from products.models import Product
from .models import CartItem,Cart
from .utils import get_cart_id
# Create your views here.


def cart_add(request:HttpRequest,product_slug : str):

    user = request.user
    product = get_object_or_404(Product,slug=product_slug)

    cart : Cart

    if request.user.is_authenticated:
        cart , _ =  Cart.objects.get_or_create(customer = user)
    else:
        cart , _ =  Cart.objects.get_or_create(cart_id = get_cart_id(request))

    item , created = CartItem.objects.get_or_create(cart=cart,product=product)
    if not created:
        item.quantity += 1
        item.save()
        return redirect(reverse('products:list'))

    return redirect(reverse('products:list'))


def cart_detail(request):

    cart : Cart

    if request.user.is_authenticated:
        cart , _ =  Cart.objects.get_or_create(customer = request.user)
    else:
        cart , _ =  Cart.objects.get_or_create(cart_id = get_cart_id(request))

    context = {
        'cart' : cart,
        'items' : cart.items.all()
    }
    return render(request,'carts/cart_detail.html',context=context)