from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/books/add', views.add_book),
    path('books/<int:book_id>', views.show_book),
    path('books/<int:book_id>/add_author_to_book', views.add_author_to_book)
]