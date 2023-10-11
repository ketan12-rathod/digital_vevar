"""vevar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from user import views
urlpatterns = [
    path('index/<str:myboy>/<str:mygirl>/', views.index, name='index'),
    path('store_vevar', views.store_vevar, name='store_vevar'),
    path('all_vevar/<int:id>/<str:girl_name>/<str:boy_name>/', views.all_vevar, name='all_vevar'),
    path('edit_vevar/<int:id>', views.edit_vevar, name='edit_vevar'),
    path('update_vevar/<int:id>', views.update_vevar, name='update_vevar'),
    path('info', views.info, name='info'),
    path('store_info', views.store_info, name='store_info'),
    path('register', views.register, name='register'),
    path('store_register', views.store_register, name='store_register'),
    path('name', views.name, name='name'),
    path('store_name', views.store_name, name='store_name'),
    path('all_name/<str:girl_name>/<str:boy_name>/', views.all_name, name='all_name'),
    
]
