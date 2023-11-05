from django.views.generic import TemplateView

from core.mixins import custom_mixin_kategorimenu

# Create your views here.

class webauth(custom_mixin_kategorimenu, TemplateView):
    ''' Class used for the webauth view '''
    template_name = 'webauth/index.html'