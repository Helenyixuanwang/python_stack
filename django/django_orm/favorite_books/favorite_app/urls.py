from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('create', views.create),
    path('books', views.success),
    path('login', views.login),
    path('logout', views.logout),
    path('add_book', views.add_book),
    path('books/<int:book_id>', views.display_book),
    path('books/<int:book_id>/update',views.update),
    path('books/<int:book_id>/delete',views.delete),
    path('books/<int:book_id>/add_favorite',views.add_favorite),
    path('books/<int:book_id>/unfavor', views.unfavor),
]