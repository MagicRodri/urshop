

from django.db import transaction
from django.forms import formset_factory
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BrandForm, ImageForm, ProductForm
from .models import Product

# Create your views here.

def product_create(request : HttpRequest) -> HttpResponse:

    # Form set to eventually grab up to 3 images for a product
    ImageFormSet = formset_factory(ImageForm,extra=3)

    product_form = ProductForm()
    image_form_set = ImageFormSet()
    brand_form = BrandForm()

    if request.method == 'POST' :
        print(request.POST)
        product_form = ProductForm(request.POST)
        image_form_set = ImageFormSet(request.POST,request.FILES)
        brand_form = BrandForm(request.POST)

        if all([product_form.is_valid(),image_form_set.is_valid(),brand_form.is_valid()]):
            product = product_form.save(commit=False)
            brand = brand_form.save()
            product.user = request.user
            product.brand = brand
            product.save()
            
            for image_form in image_form_set:
                if image_form.cleaned_data:
                    image = image_form.save(commit=False)
                    image.product = product
                    image.save()

            return redirect(product.get_absolute_url())

    context = {
        'product_form' : product_form,
        'brand_form' : brand_form,
        'image_form_set' : image_form_set
    }

    return render(request,template_name='products/product_create.html',context = context)

def product_detail(request : HttpRequest, slug : str) -> HttpResponse:
    product = get_object_or_404(Product.objects.prefetch_related('images'),slug=slug)
    product_images = product.images.all()
    
    context ={
        'product' : product,
        'main_image' : product_images.first(),
        'product_images' : product_images
    }
    return render(request,template_name='products/product_detail.html',context = context)

def product_edit(request: HttpRequest,slug : str) -> HttpResponse:
    ...
    
def product_delete(request: HttpRequest,slug : str) -> HttpResponse:

    product = get_object_or_404(Product,slug=slug)
    if request.method == 'POST':
        product.delete()
        return HttpResponse('Product deleted successfully')
    return render(request,'products/product_delete.html')

def product_list(request: HttpRequest) -> HttpResponse:

    products = Product.objects.all()

    return render(request,template_name='products/product_list.html',context={'products' : products})