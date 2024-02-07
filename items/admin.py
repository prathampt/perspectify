from django.contrib import admin
from .models import Category, Genre, Book, UserBook

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_by', 'created_at')
    list_filter = ('category', 'genre', 'created_by')
    search_fields = ('title', 'author')

@admin.register(UserBook)
class UserBookAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'has_read')
    list_filter = ('user', 'book', 'has_read')
