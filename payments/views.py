from django.shortcuts import render, redirect,get_object_or_404
from django.conf import settings
from django.http import JsonResponse,HttpRequest,HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from carts.models import Cart

import stripe

# This is your test secret API key.


stripe.api_key = settings.STRIPE_SECRET_KEY


YOUR_DOMAIN = 'http://127.0.0.1:8000'


def payments_success(request):

    return render(request,'payments/payment_success.html')

def payments_cancel(request):

    return render(request,'payments/payment_cancel.html')


def create_checkout_session(request : HttpRequest, pk : int):

    if request.method == 'POST':
        cart = get_object_or_404(Cart, pk = pk)
        items = []
        for item in cart.items.all():
            items.append(
                {
                    'price_data': {
                        'currency' : 'usd',
                        'unit_amount' : int(item.price * 100),
                        'product_data' : {
                            'name' : item.name
                            # 'images' : []
                        }
                    },
                    'quantity': item.quantity,
                }
            )
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=items,
            mode='payment',
            success_url=YOUR_DOMAIN + reverse('payments:success'),
            cancel_url=YOUR_DOMAIN + reverse('payments:cancel'),
        )
        return JsonResponse({
            'id' : checkout_session.id
        })
            
    return redirect(checkout_session.url)



@csrf_exempt
def stripe_webhook(request):
    """
        Stripe webhook view to fulfill orders 
    """
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']


    return HttpResponse(status=200)