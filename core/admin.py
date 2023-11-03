from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import artist, newsfeed, genre,mediatype

# Register models in admin

admin.site.register(artist)
admin.site.register(newsfeed)
admin.site.register(genre)
admin.site.register(mediatype)
