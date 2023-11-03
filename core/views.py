from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponseRedirect

from core.models import newsfeed

# Create your views here.

class Index(TemplateView):
    '''Class used to display the index page '''

    template_name = 'core/index.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['newsfeeds'] = newsfeed.objects.filter(status=1).order_by('-created_on')[:10]
        # return the last ten articles to template

        return context
    
    # def get(self, request, *args, **kwargs):
    #     super().get(request, *args, **kwargs)
        
    #     art_mess = "You do not have permission to delete that comment."
    #     messages.info(request, art_mess)
    #     return HttpResponseRedirect("/webauth")

class privacy(TemplateView):
    '''Class used to display the privacy policy '''

    template_name = 'core/privacy.html'