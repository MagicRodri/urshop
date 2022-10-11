
from django.contrib import admin

from .models import Address, Order
# Register your models here.

class AddressAdmin(admin.ModelAdmin):
    model = Address
    list_display = ['name','address_line_1']

admin.site.register(Address,AddressAdmin)


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['user','order_id']
    
admin.site.register(Order,OrderAdmin)