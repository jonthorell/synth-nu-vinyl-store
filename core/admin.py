from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import artist

# Register models in admin

admin.site.register(artist)
