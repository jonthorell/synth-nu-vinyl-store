from django.views.generic import TemplateView

from core.mixins import custom_mixin_kategorimenu

# Create your views here.

class checkout(custom_mixin_kategorimenu, TemplateView):
    ''' Class used for the checkout view '''
    template_name = 'checkout/index.html'