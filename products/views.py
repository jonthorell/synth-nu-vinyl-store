from django.shortcuts import render
from django.views.generic import TemplateView

from products.models import product,genre, mediatype
from django.contrib.auth.models import User

from synth.utils import custom_mixin_kategorimenu

# Create your views here.

class products(custom_mixin_kategorimenu, TemplateView):
    '''Class used to display the products '''

    template_name = 'products/index.html'
    
    model = product
    context_object_name = 'product'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['products'] = product.objects.all().order_by('-created_on')
        # return articles to template that has the corresponding kwarg (i.e. the article being displayed)
        return context
