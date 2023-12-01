
from django.shortcuts import render
from django.contrib import messages

from .forms import AddSubscriberForm



def newsletter(request):
    """ Display the staff only page. """
    
    template = 'newsletter/newsletter.html'
    
    form = AddSubscriberForm(request.POST)

    context = {"form": form}
    
    

    return render(request, template, context)