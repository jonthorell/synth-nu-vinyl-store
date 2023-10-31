from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

class Index(TemplateView):
    '''Class used to display the index page '''

    template_name = 'core/index.html'
    
    # def get(self, request, *args, **kwargs):
    #     super().get(request, *args, **kwargs)
        
    #     art_mess = "You do not have permission to delete that comment."
    #     messages.info(request, art_mess)
    #     return HttpResponseRedirect("/webauth")