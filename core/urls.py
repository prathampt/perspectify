from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm


app_name = 'core'

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('privacyPolicy/', views.privacyPolicy, name='privacyPolicy'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),

]