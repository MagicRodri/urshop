from .models import Cart, CartItem


def cart_detail(request):
    cart, _ = Cart.objects.get_or_new(request)
    return {'cart': cart,'cart_items' : cart.items.all()}