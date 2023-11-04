from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import product, genre, mediatype, artist

# Register models in admin

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'genre',
        'price',
        'rating',
        'image',
        'slug',
     )
    
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'slug',
        )
    
class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'slug',
        )
    
class MediaTypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'slug',
        )
        


admin.site.register(product, ProductAdmin)
admin.site.register(genre, GenreAdmin)
admin.site.register(mediatype, MediaTypeAdmin)
admin.site.register(artist,ArtistAdmin)
