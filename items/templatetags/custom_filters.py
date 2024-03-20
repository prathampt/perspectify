from django import template
from ..models import SaveBook

register = template.Library()

@register.filter(name='is_book_saved')
def is_book_saved(user, book):
    return SaveBook.objects.filter(user=user, book=book).exists()
