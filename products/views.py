from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
from django.db import transaction
from django.forms import formset_factory

from .forms import ProductForm,BrandForm,ImageForm
# Create your views here.



def create_product(request : HttpRequest) -> HttpResponse:

    # Form set to eventually grab up to 3 images for a product
    ImageFormSet = formset_factory(ImageForm,extra=3)

    product_form = ProductForm()
    image_form_set = ImageFormSet()
    brand_form = BrandForm()

    if request.method == 'POST' :
        product_form = ProductForm(request.POST)
        image_form_set = ImageFormSet(request.POST,request.FILES)
        brand_form = BrandForm(request.POST)

        if all([product_form.is_valid(),image_form_set.is_valid(),brand_form.is_valid()]):
            product = product_form.save(commit=False)
            brand = brand_form.save()
            product.brand = brand
            product.save()
            
            for image_form in image_form_set:
                if image_form.cleaned_data:
                    image = image_form.save(commit=False)
                    image.product = product
                    image.save()

            return HttpResponse('product save successfully')

    context = {
        'product_form' : product_form,
        'brand_form' : brand_form,
        'image_form_set' : image_form_set
    }

    return render(request,template_name='products/create_product.html',context = context)