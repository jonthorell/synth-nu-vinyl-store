from django.views.generic import TemplateView


# Create your views here.

class webauth(TemplateView):
    ''' Class used for the webauth view '''
    template_name = 'webauth/index.html'