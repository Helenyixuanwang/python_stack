from django.urls import path
from . import views

urlpatterns = [
    path('', views.allshow),
    path('new', views.newshow),
    path('create',views.create),
    path('<int:show_id>', views.show_display),
    path('<int:show_id>/edit', views.edit),
    path('<int:show_id>/update',views.update),
    path('<int:show_id>/destroy',views.delete)
]