from django.urls import path
from .views import staff

app_name = "staff"

urlpatterns = [
    path('', staff.as_view(), name='staff'),
    ]