from django.urls import path

from .views import category_list, overview

app_name = 'api'
urlpatterns = [
    path('',overview),
    path('products/category/',category_list)
]