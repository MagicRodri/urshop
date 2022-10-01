from django.urls import path

from .views import(
    product_create,
    product_detail
)

app_name = 'products'
urlpatterns = [
    path('create/',product_create,name='create'),
    path('detail/<slug:slug>',product_detail,name='detail'),

]