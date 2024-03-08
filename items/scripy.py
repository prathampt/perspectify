import os
import random
from .models import Book, User, Genre
from django.core.files import File

image_folder = 'items/randomImages/'

if not os.path.exists(image_folder):
    raise FileNotFoundError("Image folder not found. Please provide the correct path.")

# Get a list of all image files in the folder
image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
image_files.remove(".trackme")

def add_books_from_json(data):
    book_data = data

    # Extract data for each book
    title = book_data['title']
    author = book_data['author']
    genres = book_data['genre']
    stories = book_data['story']
    created_by = User.objects.first()

    image_file = random.choice(image_files)

    book = Book.objects.create(
        title=title,
        author=author,
        created_by=created_by,
        description='\n'.join(stories),
    )

    with open(os.path.join(image_folder, image_file), 'rb') as image_file_obj:
        # Create a Django File object
        django_file = File(image_file_obj)
        # Assign the File object to the image field
        book.image.save(image_file, django_file, save=True)

    for genre_name in genres:
        genre, created = Genre.objects.get_or_create(name=genre_name)
        book.genre.add(genre)

    book.save()
