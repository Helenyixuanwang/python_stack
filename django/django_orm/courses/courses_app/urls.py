from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('courses/create', views.create),
    path('courses/destroy/<int:course_id>', views.show_delete),
    path('courses/comment/<int:course_id>', views.comment)
    
]