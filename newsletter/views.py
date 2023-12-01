
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db import IntegrityError

from .models import subscription
from .forms import AddSubscriberForm



def newsletter(request):
    """ Display the newspaper page. """
    if 'subscribe' in request.POST:
        # subscribe
        form = AddSubscriberForm(request.POST)
        if form.is_valid():
            try:
                prod = form.save()
                messages.success(request, 'You are added to the mailing list!')
                return HttpResponseRedirect('/')
            except IntegrityError as e:
                # This is supposed to show an error indicating that you already is subscribed.
                # the is_valid() seems to catch that though, but leaves it here just as a precaution
                messages.error(request, 'That e-mail adress is already on record.')
                return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Failed to add you. Please ensure the form is valid.')
            return HttpResponseRedirect('/newsletter')
    elif 'unsubscribe' in request.POST:
        #unsubscribe
        
        email=request.POST.get("email","")
        
        is_subscribed = subscription.objects.filter(email=email).exists()
 
        if not is_subscribed:
            messages.error(request, 'That e-mail does not subscribe to the mailing list')
        else:
            subscription.objects.filter(email=email).delete()
            messages.info(request, 'You are now unsubscribed.')
        return HttpResponseRedirect('/')
    else:
        form = AddSubscriberForm()

    template = 'newsletter/newsletter.html'
    context = {
        'form': form,
    }

    return render(request, template, context)