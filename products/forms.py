
from django import forms 

from .models import Product,Brand,Category,Image

class ProductForm(forms.ModelForm):
    """
        Form for product creation page with the necessary fields that will be completed with other related fields forms
    """
    class Meta:
        model = Product
        fields = ['name','category','description','price','old_price','quantity']

class CategoryForm(forms.ModelForm):

    """
        Category form to be used on category creation
    """

    class Meta:
        model = Category
        fields = ['name','description']


class BrandForm(forms.ModelForm):
    """
        Brand form to be used on product creation (with product form)
    """

    class Meta:
        model = Brand
        fields = ['name']

class ImageForm(forms.ModelForm):
    """
        Image form to be used in addition with product form (only image needed)
    """

    class Meta:
        model = Image
        fields = ['image']




