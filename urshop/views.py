from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

from products.views import product_list

def home(request: HttpRequest) -> HttpResponse:

    return product_list(request)