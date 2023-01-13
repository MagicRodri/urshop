from django.urls import path

from .views import (
    product_create,
    product_delete,
    product_detail,
    product_edit,
    product_list,
)

app_name = 'products'
urlpatterns = [
    path('create/', product_create, name='create'),
    path('delete/<slug:slug>', product_delete, name='delete'),
    path('detail/<slug:slug>', product_detail, name='detail'),
    path('edit/<slug:slug>', product_edit, name='edit'),
    path('', product_list, name='list'),
]