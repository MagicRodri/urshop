from django.urls import path

from .views import(
    create_product,
)

app_name = 'products'
urlpatterns = [
    path('create/',create_product,name='create'),

]