from django.urls import path
from . import views

urlpatterns = [
    path('',views.random),
    path('random_word', views.random),
    path('reset', views.reset)
]