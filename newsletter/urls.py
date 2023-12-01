from django.urls import path

from . import views
from .views import newsletter

urlpatterns = [
    path('', views.newsletter, name='newsletter'),
]