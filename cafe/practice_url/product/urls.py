from django.urls import path
from product import views

urlpatterns = [
    path('', views.productlist), 
    path('first/', views.productfirst),   # 127.0.0.1:8000/products/first
]