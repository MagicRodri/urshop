from django.forms import formset_factory
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, TemplateView

from .forms import BrandForm, ImageForm, ProductForm
from .models import Brand, Category, Product


class ProductCreateView(TemplateView):
    template_name = 'products/product_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_form'] = ProductForm()
        context['brand_form'] = BrandForm()
        context['image_form_set'] = formset_factory(ImageForm, extra=3)
        return context

    def post(self, request, *args, **kwargs):
        product_form = ProductForm(request.POST)
        image_form_set = formset_factory(ImageForm, extra=3)(request.POST,
                                                             request.FILES)
        brand_form = BrandForm(request.POST)

        if all([
                product_form.is_valid(),
                image_form_set.is_valid(),
                brand_form.is_valid()
        ]):
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


def product_detail(request: HttpRequest, slug: str) -> HttpResponse:
    product = get_object_or_404(Product.objects.prefetch_related('images'),
                                slug=slug)
    product_images = product.images.all()

    context = {
        'product': product,
        'main_image': product_images.first(),
        'product_images': product_images
    }
    return render(request,
                  template_name='products/product_detail.html',
                  context=context)


def product_edit(request: HttpRequest, slug: str) -> HttpResponse:
    ...


def product_delete(request: HttpRequest, slug: str) -> HttpResponse:

    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        product.delete()
        return HttpResponse('Product deleted successfully')
    return render(request, 'products/product_delete.html')


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')
        if category:
            queryset = queryset.filter(category__slug__icontains=category)
        if brand:
            queryset = queryset.filter(brand__name__icontains=brand)
        return queryset