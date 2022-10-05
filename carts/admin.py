from django.contrib import admin

from .models import Cart,CartItem
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ['customer','cart_id']
    search_fields = ['customer']

admin.site.register(Cart,CartAdmin)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product','quantity','cart']

admin.site.register(CartItem,CartItemAdmin)