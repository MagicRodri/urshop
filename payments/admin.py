from django.contrib import admin

from .models import Currency, StripePayment

admin.site.register(StripePayment)
admin.site.register(Currency)
