from django.views.generic import TemplateView

# from synth.utils import custom_mixin_kategorimenu


# Create your views here.

class profile(TemplateView):
    ''' Class used for the profile view '''
    template_name = 'profiles/profiles.html'