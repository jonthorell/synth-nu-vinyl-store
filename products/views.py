from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

    #     return HttpResponseRedirect("/webauth")

class products(TemplateView):
    '''Class used to display the products '''

    template_name = 'products/index.html'
