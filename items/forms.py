from django import forms
from .models import Book

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'genre', 'description', 'image',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'custom-form-input',
                'placeholder': 'Enter title'
            }),
            'author': forms.TextInput(attrs={
                'class': 'custom-form-input',
                'placeholder': 'Enter author'
            }),
            'genre': forms.SelectMultiple(attrs={
                'class': 'custom-form-input'
            }),
            'description': forms.Textarea(attrs={
                'class': 'custom-form-input',
                'placeholder': 'Enter description'
            }),
            'image': forms.FileInput(attrs={
                'class': 'custom-form-input',
                'placeholder': 'Upload image'
            })
        }

class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'genre', 'description', 'image',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'custom-form-input',
                'placeholder': 'Enter title'
            }),
            'author': forms.TextInput(attrs={
                'class': 'custom-form-input',
                'placeholder': 'Enter author'
            }),
            'genre': forms.SelectMultiple(attrs={
                'class': 'custom-form-input'
            }),
            'description': forms.Textarea(attrs={
                'class': 'custom-form-input',
                'placeholder': 'Enter dcription'
            }),
            'image': forms.FileInput(attrs={
                'class': 'custom-form-input',
                'placeholder': 'Upload image'
            })
        }
