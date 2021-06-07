from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create_note),
    path('create_ajax',views.create_ajax),
    path('edit/<int:note_id>', views.edit_note),
    path('delete',views.delete),
    path('delete_ajax',views.delete_ajax),
    path('update/<int:note_id>',views.update),
    # path('display', views.display)
]