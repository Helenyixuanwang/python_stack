from django.urls import path
from . import views

urlpatterns = [
    path('welcome', views.welcome),
    path('', views.register),
    path('login_page',views.login_page),
    path('logout_user',views.logout_user)
    
]