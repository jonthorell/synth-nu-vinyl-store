from django.views.generic import TemplateView


# Create your views here.

class profile(TemplateView):
    ''' Class used for the profile view '''
    template_name = 'profiles/index.html'