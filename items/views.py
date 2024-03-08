from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Genre, Book
from .forms import AddBookForm, EditBookForm
from .scripy import add_books_from_json
import json, os

def books(request):
    genres = Genre.objects.all()
    genre_id = request.GET.get('genre', 0)
    query = request.GET.get('query', '')

    books = Book.objects.all()

    if genre_id and genre_id != "0":
        books = books.filter(genre__id=genre_id)

    if query:
        query_words = query.split()

        query_filter = Q()
        for word in query_words:
            query_filter |= Q(title__icontains=word) | Q(author__icontains=word)

        books = books.filter(query_filter)


    return render(request, 'items/books.html', {
        'books': books,
        'query': query,
        'genres': genres,
        'genre_id': int(genre_id)
    })

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    related_books = Book.objects.filter(genre__in=book.genre.all()).exclude(pk=pk)[0:3]

    return render(request, 'items/detail.html', {
        'book': book,
        'related_books': related_books
    })

@login_required
def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES)

        if form.is_valid():
            print("The form is valid")
            book = form.save(commit=False)
            book.created_by = request.user
            book.save()
            genres = request.POST.getlist('genres')
            book.genre.set(genres)

            return redirect('items:book_detail', pk=book.pk)
        else:
            print("The form is not valid")
            print(form.errors)
    else:
        form = AddBookForm()

    return render(request, 'items/forms.html', {
        'form': form,
        'title': 'Add Book',
    })

@login_required
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditBookForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            edited_book = form.save(commit=False)
            edited_book.save()  # Save the book instance first to ensure it has a primary key

            # Update the genres
            genres = request.POST.getlist('genres')
            edited_book.genre.set(genres)

            return redirect('items:book_detail', pk=book.pk)
    else:
        form = EditBookForm(instance=book)

    return render(request, 'items/forms.html', {
        'form': form,
        'title': 'Edit Book',
    })


@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk, created_by=request.user)
    book.delete()

    return redirect('items:books')

def automation(request):
    folder_path = 'items/data/'

    json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

    for json_file in json_files:
        with open(os.path.join(folder_path, json_file), 'r') as f:
            data = json.load(f)
            add_books_from_json(data)

    return redirect('items:books')
