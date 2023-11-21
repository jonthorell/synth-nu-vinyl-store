from django.urls import path
from .views import checkout
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    ]