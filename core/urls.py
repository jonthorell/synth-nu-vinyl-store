

from . import views
from django.urls import path


urlpatterns = [
    path("", views.Index.as_view(), name="Index"),
    path("privacy", views.privacy.as_view(), name="privacy"),
    path("contact", views.contact.as_view(), name="contact"),
    path('newsadd/', views.add_news, name='add_news'),
    path('editnews/<int:news_id>/', views.editnews, name='editnews'),
    path('deletenews/<int:product_id>/', views.deletenews, name='deletenews'),
]