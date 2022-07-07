import imp
from django.contrib import admin
from django.urls import path, include   # include가 하위 url 관리 추가
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first),
    path('second/', views.second),
    path('products/', include('product.urls')),
    path('boards/', include('board.urls')),
]