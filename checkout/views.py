from django.views.generic import TemplateView

# Create your views here.

class checkout(TemplateView):
    ''' Class used for the checkout view '''
    template_name = 'checkout/checkout.html'