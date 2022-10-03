
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpRequest
from django.urls import reverse

from products.models import Product
from .models import CartItem,Cart
# Create your views here.


def cart_add(request:HttpRequest,product_slug : str):

    user = request.user
    product = get_object_or_404(Product,slug=product_slug)

    cart , _ = Cart.objects.get_or_create(customer = user)

    item , created = CartItem.objects.get_or_create(cart=cart,customer=user,product=product)
    if not created:
        item.quantity += 1
        item.save()
        return redirect(reverse('carts:detail'))

    return render(request,'carts/cart_add.html')


def cart_detail(request):

    cart =  get_object_or_404(Cart,customer = request.user)
    context = {
        'cart' : cart,
        'items' : cart.items.all()
    }
    return render(request,'carts/cart_detail.html',context=context)