from django.contrib.auth.models import User
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Genres'
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.ManyToManyField(Genre, related_name='books', blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='book_images', blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class SaveBook(models.Model):
    user = models.ForeignKey(User, related_name='user_books', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='user_books', on_delete=models.CASCADE)
      

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"

