from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Order, OrderLineItem

# Register models in admin

class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_number',
        'full_name',
        'email',
        'phone_number',
        'country',
        'postcode',
        'street_address1',
        'street_address2',
        'county',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',
     )
 
admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderLineItem, OrderAdmin)