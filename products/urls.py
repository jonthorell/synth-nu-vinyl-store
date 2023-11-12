


from django.urls import path
from . import views
# from .views import all_products, product_detail

urlpatterns = [
    path("", views.all_products.as_view(), name="products"),
    path('<product_id>', views.product_detail, name='product_detail'),
]