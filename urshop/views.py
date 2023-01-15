from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from products.models import Category, Product


def home(request: HttpRequest) -> HttpResponse:
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request,'home.html',context)