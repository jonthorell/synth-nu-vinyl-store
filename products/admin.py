from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import product, genre, mediatype, artist

# Register models in admin

admin.site.register(product)
admin.site.register(genre)
admin.site.register(mediatype)
admin.site.register(artist)
