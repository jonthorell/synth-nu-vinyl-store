from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import newsfeed, contact_message

# Register models in admin

class contact_messageAdmin(admin.ModelAdmin):
    list_display = (
        'subjectline',
        'name',
        'created_on',
        'complete',
        'email',
        'slug',
     )

admin.site.register(newsfeed)
admin.site.register(contact_message, contact_messageAdmin)

