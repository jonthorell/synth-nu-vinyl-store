from django.urls import path
from . import views

app_name = "staff"

urlpatterns = [
    path('', views.staff, name='staff'),
    path('view_orders', views.view_orders, name='view_orders'),
    ]