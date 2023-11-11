from django.views.generic import TemplateView

from synth.utils import StaffRequiredMixin

# Create your views here.

class staff(StaffRequiredMixin, TemplateView):
    ''' Class used for the staff view '''
    template_name = 'staff/index.html'