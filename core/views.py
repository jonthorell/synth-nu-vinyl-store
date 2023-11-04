from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from .models import newsfeed
from products.models import product,genre,mediatype

# Create your views here.

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


class Index(custom_mixin_kategorimenu, TemplateView):
    '''Class used to display the index page '''

    template_name = 'core/index.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['newsfeeds'] = newsfeed.objects.filter(status=1).order_by('-created_on')[:10]
        context['products'] = product.objects.all().order_by('-created_on')[:10]
        # return the last ten articles to template

        return context
    
    # def get(self, request, *args, **kwargs):
    #     super().get(request, *args, **kwargs)
        
    #     art_mess = "You do not have permission to delete that comment."
    #     messages.info(request, art_mess)
    #     return HttpResponseRedirect("/webauth")

class privacy(custom_mixin_kategorimenu, TemplateView):
    '''Class used to display the privacy policy '''

    template_name = 'core/privacy.html'
    
class contact(custom_mixin_kategorimenu, TemplateView):
    '''Class used to display the contact form '''

    template_name = 'core/contact.html'