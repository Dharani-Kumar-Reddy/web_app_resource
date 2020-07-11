from django.contrib import admin
from django.urls import path,re_path
from . import views

urlpatterns = [
   
    path('login', views.Adminlogin, name="admin"),
    path('register', views.register, name="register"),
    path('details', views.details, name="details"),


    
    
]