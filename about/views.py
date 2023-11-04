from django.views.generic import TemplateView

from products.models import product,genre, mediatype
from django.contrib.auth.models import User


# Create your views here.

class custom_mixin_kategorimenu(object):
    '''Used to make all the context_data available at all times so the author/categories menues can be populated '''

    # all other classes needs this mixin

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
        except AttributeError:
            context = {}
        
        context['mediatypes'] = mediatype.objects.all()
        context['genres'] = genre.objects.all()
        context['users'] = User.objects.prefetch_related("groups")
        return context

class about(custom_mixin_kategorimenu, TemplateView):
    ''' Class used for the about view '''
    template_name = 'about/index.html'
    
