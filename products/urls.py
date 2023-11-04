

from . import views
from django.urls import path
from .views import products

urlpatterns = [
    path("", views.products.as_view(), name="products"),
]