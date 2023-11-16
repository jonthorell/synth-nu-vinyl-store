from django.views.generic import TemplateView
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
import freecurrencyapi

# Create your views here.

def checkout(request):
    client = freecurrencyapi.Client(settings.CURRENCY_API_KEY)
    result = client.currencies(currencies=['EUR', 'CAD', 'SEK'])
    
    context = {
        'currency': result,
    }
    
    return render(request, 'checkout/checkout.html', context)