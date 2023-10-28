from django.views.generic import TemplateView


# Create your views here.

class about(TemplateView):
    ''' Class used for the about view '''
    template_name = 'about/index.html'