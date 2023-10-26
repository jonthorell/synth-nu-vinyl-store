from django.urls import path
from .views import webauth

app_name = "webauth"

urlpatterns = [
    path('', webauth.as_view(), name='webauth'),
    ]