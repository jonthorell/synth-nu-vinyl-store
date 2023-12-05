from django.urls import path
from . import views

app_name = "staff"

urlpatterns = [
    path('', views.staff, name='staff'),
    path('view_orders', views.view_orders, name='view_orders'),
    path("approve_review", views.approve_review, name="approve_review"),
    path('approve/<int:review_id>/', views.update_review, name='update_review'),
    ]