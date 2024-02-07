from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('', views.books, name='books'),
    path('new/', views.add_book, name='add_book'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('<int:pk>/delete/', views.delete_book, name='delete_book'),
    path('<int:pk>/edit/', views.edit_book, name='edit_book'),
]
