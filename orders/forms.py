
from django import forms

from .models import Order, Address


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ['name','address_type','address_line_1','address_line_2','country','state','city','zip']
        # widgets = {
        #     'name' : forms.TextInput(attrs={
        #         'class' : 'form-control md-12',
        #     })
        # }
class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = []