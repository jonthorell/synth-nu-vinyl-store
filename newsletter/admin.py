from django.contrib import admin

from django.contrib.auth.models import User
from .models import subscription

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        )
    
admin.site.register(subscription,SubscriptionAdmin)
