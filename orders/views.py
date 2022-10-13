
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from carts.models import Cart
from core.utils import get_user_id

from .forms import AddressForm
from .models import Address, Order

# Create your views here.

@login_required()
def order_create(request : HttpRequest):

    address_form = AddressForm()
    cart , _ = Cart.objects.get_or_new(request)

    context = {
        'address_form' : address_form,
        'cart' : cart,
        'items' : cart.items.all(),
        'STRIPE_PUBLIC_KEY' : settings.STRIPE_PUBLIC_KEY
    }

    if request.method == 'POST':

        address_form = AddressForm(request.POST)

        if address_form.is_valid():

            address = address_form.save()

            order = Order.objects.create(
                address = address,
                cart = cart
            )

            if request.user.is_authenticated:
                order.user = request.user
                order.save()
            else:
                order.order_id = get_user_id(request)
                order.save()
            return JsonResponse({
                'success' : True
            })

    return render(request,'orders/order_create.html', context = context)