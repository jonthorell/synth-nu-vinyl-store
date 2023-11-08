from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from .models import newsfeed
from products.models import product,genre,mediatype

from synth.utils import custom_mixin_kategorimenu

# Create your views here.



class Index(custom_mixin_kategorimenu, TemplateView):
    '''Class used to display the index page '''

    template_name = 'core/index.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['newsfeeds'] = newsfeed.objects.filter(status=1).order_by('-created_on')[:10]
        context['products'] = product.objects.all().order_by('-created_on')[:10]
        # return the last ten products as well as the last ten newsitems to template

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
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        # return articles to template that has the corresponding kwarg (i.e. the article being displayed)
        return context
    
    def get(self, request, *args, **kwargs):
        # display the form
        context = self.get_context_data()
        messages.error(request, "Your comment has been added.")
        
        return HttpResponseRedirect("/")
