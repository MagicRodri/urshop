from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
from django.db import transaction

from .forms import ProductForm,BrandForm,ImageForm
# Create your views here.



def create_product(request : HttpRequest) -> HttpResponse:

    product_form = ProductForm()
    image_form = ImageForm()
    brand_form = BrandForm()

    if request.method == 'POST' :
        product_form = ProductForm(request.POST)
        image_form = ImageForm(request.POST,request.FILES)
        brand_form = BrandForm(request.POST)

        if all([product_form.is_valid(),image_form.is_valid(),brand_form.is_valid()]):
            product = product_form.save(commit=False)
            brand = brand_form.save()
            product.brand = brand
            product.save()
            image = image_form.save(commit=False)
            image.product = product
            image.save()

            return HttpResponse('product save successfully')

    context = {
        'product_form' : product_form,
        'brand_form' : brand_form,
        'image_form' : image_form
    }

    return render(request,template_name='products/create_product.html',context = context)