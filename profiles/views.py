from django.views.generic import TemplateView

from core.mixins import custom_mixin_kategorimenu


# Create your views here.

class profile(custom_mixin_kategorimenu, TemplateView):
    ''' Class used for the profile view '''
    template_name = 'profiles/index.html'