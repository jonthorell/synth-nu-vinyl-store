from collections import UserString
from django.db.models import CharField, Model
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from autoslug import AutoSlugField

STATUS = ((0, "Draft"), (1,"Published"))
User=get_user_model()

class artist(models.Model):
    '''Class used to create the artists model '''

    name = models.CharField(max_length=40, blank=False, null=False, unique=True)
    short_name = models.CharField(max_length=40, blank=False, null=False, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.CharField(max_length=200, blank=False, null=False)
    artist_image = models.CharField(max_length=60, blank=False, null=False, default="empty-artist-image.png")

    class Meta:
        ordering = ['name']

    def __str__ (self):
        return self.name

    def get_absolute_url(self):
        return reverse("articles_by_category", args=[str(self.id)])
    
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