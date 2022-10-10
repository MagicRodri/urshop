from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Order, Address
from .forms import AddressForm
from carts.models import Cart
# Create your views here.


def order_create(request : HttpRequest):

    address_form = AddressForm()
    cart , _ = Cart.objects.get_or_new(request)
    if request.method == 'POST':
        address_form = AddressForm(request.POST)
        if address_form.is_valid():
            address = address_form.save()
            order = Order.objects.create(
                address = address,
                cart = cart
            )

            return HttpResponse('Order submitted')
    context = {
        'address_form' : address_form,
        'cart' : cart,
        'items' : cart.items.all()
    }
    return render(request,'orders/order_create.html', context = context)