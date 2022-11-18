from django.urls import path

from .views import cart_add, cart_decrement, cart_detail, cart_remove

app_name = 'carts'
urlpatterns = [
    path('detail/',cart_detail,name='detail'),
    path('add/<slug:product_slug>/',cart_add,name='add'),
    path('decrement/<slug:product_slug>/',cart_decrement,name='decrement'),
    path('remove/<int:item_pk>/',cart_remove,name='remove'),
]