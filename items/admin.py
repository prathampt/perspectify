from django.contrib import admin
from .models import Genre, Book, SaveBook

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_by', 'created_at')
    list_filter = ('genre', 'created_by')
    search_fields = ('title', 'author')

@admin.register(SaveBook)
class UserBookAdmin(admin.ModelAdmin):
    list_display = ('user', 'book')
    list_filter = ('user', 'book')
