from django.views.generic import TemplateView

from core.mixins import custom_mixin_kategorimenu

# Create your views here.

class staff(custom_mixin_kategorimenu, TemplateView):
    ''' Class used for the staff view '''
    template_name = 'staff/index.html'