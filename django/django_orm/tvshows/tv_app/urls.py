from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.allshow),
    path('shows/new', views.newshow),
    path('shows/create',views.create),
    path('shows/<int:show_id>', views.show_display),
    path('shows/<int:show_id>/edit', views.edit),
    path('shows/<int:show_id>/update',views.update),
    path('shows/<int:show_id>/destroy',views.delete)
]