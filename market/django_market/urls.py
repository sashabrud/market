"""django_market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.CategoryListView.as_view(), name = 'index'),
    path('categories/<int:pk/>', views.CategoryDetail.as_view(), name = 'categories'),
    path('categories/products/', views.ProductListView.as_view(), name = 'product_list'),
    path('categories/products/<int:pk>/', views.ProductDetail.as_view(), name = 'product detail'),

    
]
