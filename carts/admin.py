from django.contrib import admin

from .models import Cart, CartItem

# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ['user','cart_id','is_active']
    search_fields = ['user']

admin.site.register(Cart,CartAdmin)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product','quantity','cart']

admin.site.register(CartItem,CartItemAdmin)