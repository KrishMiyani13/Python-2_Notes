from django.urls import path
from product.views import product_list

urlpatterns = [
    path('products/',product_list)
]