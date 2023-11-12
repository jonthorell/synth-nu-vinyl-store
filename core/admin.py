from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import newsfeed, contact_message

# Register models in admin

admin.site.register(newsfeed)
admin.site.register(contact_message)

