from django import forms

from .models import Address, Order


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = [
            'first_name', 'last_name', 'email','address_type', 'address_line_1', 'address_line_2', 'country','state', 'city', 'zip'
        ]
        widgets = {
            'address_type': forms.Select(attrs={
                'class': 'form-select'}),
        }
class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = []