from django.urls import path
from .views import bag

app_name = "bag"

urlpatterns = [
    path('', bag.as_view(), name='bag'),
    ]