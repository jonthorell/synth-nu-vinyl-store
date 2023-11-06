

# This files "resides" on the project level and is imported in views.py in the other apps
# It consists of helper-classes that are needed in many places and is used in this manner
# to stick to the DRY principle.

from products.models import product,genre,mediatype
from django.contrib.auth.models import User


class custom_mixin_kategorimenu(object):
    '''Used to make all the context_data available at all times so the author/categories menues can be populated '''

    # all other classes needs this mixin

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
        except AttributeError:
            context = {}
        
        context['genres'] = genre.objects.all()
        context['mediatypes'] = mediatype.objects.all()
        context['users'] = User.objects.prefetch_related("groups")
        return context
