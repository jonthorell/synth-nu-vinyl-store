from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

class Index(TemplateView):
    '''Class used to display the index page '''

    template_name = 'core/index.html'