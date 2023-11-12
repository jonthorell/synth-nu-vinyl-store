from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from products.models import product,genre, mediatype
from django.contrib.auth.models import User

# from synth.utils import custom_mixin_kategorimenu

# Create your views here.

class all_products(TemplateView):
    '''Class used to display all the products '''

    template_name = 'products/products.html'
    
    model = product
    context_object_name = 'product'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['products'] = product.objects.all().order_by('-created_on')
        # return articles to template that has the corresponding kwarg (i.e. the article being displayed)
        return context

def product_detail(request, product_id):
    """ A view to show individual product details """

    prod = get_object_or_404(product, pk=product_id)

    context = {
        'product': prod,
    }

    return render(request, 'products/product_details.html', context)