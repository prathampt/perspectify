from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'items'

urlpatterns = [
    path('', views.books, name='books'),
    path('new/', views.addBook, name='add_book'),
    path('automation/', views.automation, name='automation'),
    path('<int:pk>/', views.bookDetail, name='book_detail'),
    path('<int:pk>/delete/', views.deleteBook, name='delete_book'),
    path('<int:pk>/edit/', views.editBook, name='edit_book'),
    path('<int:pk>/save/', views.saveBook, name='save_book'),
    path('<int:pk>/unsave/', views.unSaveBook, name='unsave_book'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
