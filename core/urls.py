

from . import views
from django.urls import path
from .views import Index, privacy, contact

urlpatterns = [
    path("", views.Index.as_view(), name="Index"),
    path("privacy", views.privacy.as_view(), name="privacy"),
    path("contact", views.contact.as_view(), name="contact"),
]