from django.views.generic import TemplateView

from synth.utils import custom_mixin_kategorimenu

# Create your views here.

class about(custom_mixin_kategorimenu, TemplateView):
    ''' Class used for the about view '''
    template_name = 'about/index.html'
    
