from django.shortcuts import render,redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django import forms
from django.views.generic import TemplateView,View
from core.forms import ContactForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

from .models import newsfeed
from products.models import product,genre,mediatype


class Index(TemplateView):
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

class privacy(TemplateView):
    '''Class used to display the privacy policy '''

    template_name = 'core/privacy.html'
    
class contact(View):
    '''Class used to display the contact page '''


    def post(self, request, *args, **kwargs):
        # display form
        form = ContactForm(request.POST)
        if form.is_valid():
            # notify user
            messages.info(request, "Thank you. Your response has been logged.")
            # get form values into variables
            req_user = request.POST.get("name")
            req_mess = request.POST.get("mess")
            req_email = request.POST.get("email")
            req_subject = request.POST.get("subject")

            # set variables for e-mail.
            subject = 'Mail from Synth.Nu'
            message = f'Hi { req_user }, your issue has been received. We will look into it as soon as possible.\nThe message you submitted was { req_mess }. with the subject line { req_subject }'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [req_email, ]
            # send the mail. Notify the user and return to start page
            send_mail( subject, message, email_from, recipient_list )
            messages.info(request, "Check your e-mail.")
            return HttpResponseRedirect("/")
    def get(self, request, *args, **kwargs):
        # display form
        # context = self.get_context_data()
        form = ContactForm(request.POST)
        return render(
        request,
        "core/contact.html",
        {"form": form},
    )