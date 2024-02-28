from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default="")
    username = models.CharField(max_length=20, default="")
    email = models.EmailField(default="")
    interests = models.CharField(max_length=200)
    about_me = models.TextField()
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
