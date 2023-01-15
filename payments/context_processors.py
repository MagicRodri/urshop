from .models import Currency


def currency(request):
    currencies = Currency.objects.all()
    active_currency = currencies.first()
    return {'active_currency':active_currency,'currencies': currencies}