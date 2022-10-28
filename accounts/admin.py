from django.contrib import admin

from .models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['username','is_active']
    search_fields = ['username']

admin.site.register(User,UserAdmin)
