from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages

from .forms import OrderForm

import freecurrencyapi

# Create your views here.

def checkout(request):
    client = freecurrencyapi.Client(settings.CURRENCY_API_KEY)
    result = client.currencies(currencies=['EUR', 'CAD', 'SEK'])
    
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'currency': result,
    }

    
    return render(request, 'checkout/checkout.html', context)