from django.urls import path

from .views import (
    cart_add,
    cart_detail
)

app_name = 'carts'
urlpatterns = [
    path('detail/',cart_detail,name='detail'),
    path('add/<slug:product_slug>/',cart_add,name='add'),
]