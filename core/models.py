from collections import UserString
from django.db.models import CharField, Model
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from autoslug import AutoSlugField

# status is used to check wheter approved to be shown (newsfeed items, testimonials). Some of this has been adapted for 
# my own use from the codestar code-along
# Newsfeed items have their status automatically set to published (although can be changed). If not changed, it is immediately visible. 

# Testimonials are in draft status by default. That means an admin has to approve the comment before it can be seen



STATUS = ((0, "Draft"), (1,"Published"))
MEDIA_STATUS = ((0, "New"), (1,"Second hand"))
PROGRESS = ((0, "Not complete"), (1,"Completed"))
User=get_user_model()
    
class newsfeed(models.Model):
    '''Class used to create the newsfeed model '''

    title = models.CharField(max_length=60, blank=False, null=False, unique=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    description = models.CharField(max_length=255, blank=False, null=False)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
    
    def get_status(self):
        return self.status
    
class contact_message(models.Model):
    '''Class used to create the model used to store messages from the contact form into the db'''

    name = models.CharField(max_length=200, blank=False, null=False, unique=True)
    complete = models.IntegerField(choices=PROGRESS, default=0)
    slug = AutoSlugField(populate_from='name', unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=200, blank=False, null=False, unique=False)
    subjectline = models.CharField(max_length=200, blank=False, null=False, unique=False)
    user_message = models.CharField(max_length=200, blank=False, null=False, unique=False)
    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name
