from django.contrib import admin

from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'default_phone_number',
        'default_country',
        'default_postcode',
        'default_town_or_city',
        'default_street_address1',
        'default_street_address2',
        'default_county',
        'image',
        )
    
admin.site.register(UserProfile,UserProfileAdmin)
