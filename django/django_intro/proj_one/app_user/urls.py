from django.urls import path     
from . import views

app_name = 'users'

urlpatterns = [
    path('register', views.create_user),
    path('login', views.login),
    path('users/new', views.create_user),
    path('users',views.display),
]