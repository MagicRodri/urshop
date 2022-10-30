
from django import forms
from django.core.exceptions import ValidationError

from .models import Brand, Category, Image, Product


class ProductForm(forms.ModelForm):
    """
        Form for product creation page with the necessary fields that will be completed with other related fields forms
    """
    class Meta:
        model = Product
        fields = ['name','category','description','price','old_price','quantity']



    # def clean_quantity(self):
    #     quantity = self.cleaned_data.get('quantity')

    #     if quantity < 0 :
    #         raise ValidationError('Quantity can not be negative')
    #     elif not isinstance(quantity,int):
    #         raise ValidationError('Quantity must be positive integer')

    #     return quantity

        
    def clean(self):
        data = self.cleaned_data

        name = data.get('name')
        description = data.get('description')
        
        qs = Product.objects.filter(name = name,description = description)
        if qs.exists():
            raise ValidationError('A product with the same name and description already exists')

        return data

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
    custom_names = {'name': 'brand-name'}

    def add_prefix(self, field_name):
        field_name = self.custom_names.get(field_name, field_name)
        return super().add_prefix(field_name)

    # name.widget.attrs.update({'name': 'brand-name'})
    
    class Meta:
        model = Brand
        fields = ['name']
        # widgets = {
        #     'name' : forms.TextInput(attrs={
        #         'name' : 'brand-name'
        #     })
        # }

class ImageForm(forms.ModelForm):
    """
        Image form to be used in addition with product form (only image needed)
    """

    class Meta:
        model = Image
        fields = ['image']




