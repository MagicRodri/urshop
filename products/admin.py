from django.contrib import admin

from .models import Product,Category,Brand,Image
# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    list_display =  ['brand_name']
    search_fields = ['brand_name']

admin.site.register(Brand,BrandAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','description','created','modified']
    search_fields = ['name','description']

admin.site.register(Category,CategoryAdmin)

admin.site.register(Product)

admin.site.register(Image)
