from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'custom-form-input'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'custom-form-input'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('name', 'username', 'email', 'password1', 'password2', 'place', 'interests', 'about_me', 'language')
    
    name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your full name.',widget=forms.TextInput(attrs={
        'placeholder': 'Your name',
        'class': 'custom-form-input'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'custom-form-input'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'custom-form-input'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'custom-form-input'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'custom-form-input'
    }))
    place = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Your location',
        'class': 'custom-form-input'
    }))
    interests = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'placeholder': 'Your interests',
        'class': 'custom-form-input'
    }))
    about_me = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'About me',
        'class': 'custom-form-input'
    }))
    language = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your language',
        'class': 'custom-form-input'
    }))