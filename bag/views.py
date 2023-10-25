from django.views.generic import TemplateView


# Create your views here.

class bag(TemplateView):
    ''' Class used for the bag view '''
    template_name = 'bag/index.html'