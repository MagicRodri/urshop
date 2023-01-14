from django.urls import path

from .views import (
    ProductCreateView,
    ProductListView,
    product_delete,
    product_detail,
    product_edit,
)

app_name = 'products'
urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='create'),
    path('delete/<slug:slug>', product_delete, name='delete'),
    path('detail/<slug:slug>', product_detail, name='detail'),
    path('edit/<slug:slug>', product_edit, name='edit'),
    path('', ProductListView.as_view(), name='list'),
]