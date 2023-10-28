from django.views.generic import TemplateView


# Create your views here.

class staff(TemplateView):
    ''' Class used for the staff view '''
    template_name = 'staff/index.html'