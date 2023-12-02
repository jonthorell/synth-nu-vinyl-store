
from collections import UserString
from django.db.models import CharField, IntegerField, Model
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from autoslug import AutoSlugField

# status is used to check wheter approved to be shown (newsfeed items, testimonials). Some of this has been adapted for 
# my own use from the codestar code-along
# Newsfeed items have their status automatically set to published (although can be changed). If not changed, it is immediately visible. 

# Testimonials are in draft status by default. That means an admin has to approve the comment before it can be seen

# Media_status is used in the products model to set if the entry is brand new or used. Defaults to new.

MEDIA_STATUS = ((0, "New"), (1,"Second hand"))
MEDIA_COLOR = ((0,"Black"), (1,"Gold"), (2,"Red"),(3,"Green"),(4,"Picture"),(5,"Transparant"),(6,"Blue"))
User=get_user_model()

# Create your models here.

class genre(models.Model):
    '''Class used to create the genre model '''

    name = models.CharField(max_length=40, blank=False, null=False, unique=True)
    friendly_name = models.CharField(max_length=40, blank=False, null=False, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='friendly_name', unique=True)
    description = models.CharField(max_length=200, blank=False, null=False)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['friendly_name']

    def __str__ (self):
        return self.friendly_name

    def get_absolute_url(self):
        return reverse("articles_by_category", args=[str(self.id)])
    
    def get_friendly_name(self):
        return self.friendly_name

class product(models.Model):
    '''Class used to create the genre model '''
    # This class is based on, but modified, on the class from the boutique ado walkthru
    
    name = models.CharField(max_length=254)
    artist = models.ForeignKey('artist', null=True, blank=False, on_delete=models.SET_NULL)
    description = models.TextField()
    genre = models.ForeignKey('genre', null=True, blank=False, on_delete=models.SET_NULL)
    new_old = models.IntegerField(choices=MEDIA_STATUS, default=0)
    media_format = models.ForeignKey('mediatype', null=True, blank=False, on_delete=models.SET_NULL)
    media_color = IntegerField(choices=MEDIA_COLOR, default=0)
    sku = models.CharField(max_length=254, null=False, blank=False, default="change this")
    slug = AutoSlugField(populate_from='name', unique=True)
    price = models.DecimalField(max_digits=3, decimal_places=0)
    # price is entered as USD. API calls will be able to change this
    price_currency = models.CharField(max_length=3, null=False, blank=False,default="USD")
    rating = models.DecimalField(max_digits=1, decimal_places=0, null=False, blank=False, default=0)
    image = models.ImageField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    stock = models.IntegerField(null=False, blank=False, default=1)

    def __str__(self):
        return self.name
    
class mediatype(models.Model):
    '''Class used to create the mediatype model '''

    name = models.CharField(max_length=40, blank=False, null=False, unique=True)
    friendly_name = models.CharField(max_length=40, blank=False, null=False, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='friendly_name', unique=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['friendly_name']

    def __str__ (self):
        return self.friendly_name

    def get_absolute_url(self):
        return reverse("articles_by_category", args=[str(self.id)])
    
class artist(models.Model):
    '''Class used to create the artists model '''

    friendly_name = models.CharField(max_length=40, blank=False, null=False, unique=True)
    name = models.CharField(max_length=40, blank=False, null=False, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='friendly_name', unique=True)
    description = models.CharField(max_length=200, blank=False, null=False)

    class Meta:
        ordering = ['friendly_name']

    def __str__ (self):
        return self.friendly_name

    def get_absolute_url(self):
        return reverse("articles_by_category", args=[str(self.id)])
    
class testimonial(models.Model):
    '''Class used to create the testimonaials/reviews model '''

    reviewed = models.ForeignKey(product, on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user')
    body = models.TextField(max_length=200,blank=False, null=False)
    slug = AutoSlugField(populate_from='name', unique=False)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return (
            f"User: {self.name}, "
            f"body: {self.body[:30]}..., "
            f"({self.created_on:%Y-%m-%d %H:%M}): "
        )
