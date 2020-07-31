from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name="Index Page"),
    path('registerpage', views.registerpage,name="Register Page"),
    path('loginpage', views.loginpage,name="Login Page"),
    path('handleregister', views.handleregister,name="Handle Register"),
    path('handlelogin', views.handlelogin,name="Handle Login"),
    path('handlelogout', views.handlelogout,name="Handle Logout"),
    path('homepage', views.homepage,name="Homepage"),
    path('handledata', views.handledata,name="handle data")
]