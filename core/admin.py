from django.contrib import admin
from .models import UserProfile 

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'interests', 'about_me', 'language')
