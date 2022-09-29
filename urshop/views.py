from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def home(request: HttpRequest) -> HttpResponse:

    return render(request,template_name='index.html')