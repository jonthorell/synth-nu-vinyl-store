from django.views.generic import TemplateView

from core.mixins import custom_mixin_kategorimenu

# Create your views here.

class bag(custom_mixin_kategorimenu, TemplateView):
    ''' Class used for the bag view '''
    template_name = 'bag/index.html'