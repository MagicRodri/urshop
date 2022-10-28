from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from products.models import Category


def home(request: HttpRequest) -> HttpResponse:

    return render(request,'home.html',{'categories' : Category.objects.all().order_by('name')})