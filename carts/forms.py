
from django.forms import ModelForm

from .models import CartItem


class CartItemUpdateForm(ModelForm):

    class Meta:
        model = CartItem
        fields = ['quantity']