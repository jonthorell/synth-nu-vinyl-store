

from . import views
from django.urls import path
from .views import Index

urlpatterns = [
    path("", views.Index.as_view(), name="Index"),
]