from django.contrib import admin

from .models import Product,Category,Brand,Image
from .forms import BrandForm
# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    list_display =  ['name']
    search_fields = ['name']

admin.site.register(Brand,BrandAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','created','modified']
    search_fields = ['name','description']
    prepopulated_fields= {'slug':('name',)}
    
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','old_price']
    list_display_links = ['name']
    search_fields = ['name','description']
    prepopulated_fields= {'slug':('name',)}

admin.site.register(Product,ProductAdmin)

admin.site.register(Image)
