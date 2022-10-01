
from django import forms 
from django.core.exceptions import ValidationError

from .models import Product,Brand,Category,Image

class ProductForm(forms.ModelForm):
    """
        Form for product creation page with the necessary fields that will be completed with other related fields forms
    """
    class Meta:
        model = Product
        fields = ['name','category','description','price','old_price','quantity']

    
    # def clean(self):
    #     data = self.cleaned_data

    #     name = data.get('name')
    #     description = data.get('description')
        
    #     qs = Product.objects.filter(name = name,description = description)
    #     if qs.exists():
    #         raise ValidationError('A product with the same name and description already exists')

    #     return data

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')

        if quantity < 0 :
            raise ValidationError('Quantity can not be negative')
        elif not isinstance(quantity,int):
            raise ValidationError('Quantity must be positive integer')

        return quantity

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
        fields = ['brand_name']

class ImageForm(forms.ModelForm):
    """
        Image form to be used in addition with product form (only image needed)
    """

    class Meta:
        model = Image
        fields = ['image']



