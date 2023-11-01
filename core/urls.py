

from . import views
from django.urls import path
from .views import Index, privacy

urlpatterns = [
    path("", views.Index.as_view(), name="Index"),
    path("privacy", views.privacy.as_view(), name="privacy"),
]