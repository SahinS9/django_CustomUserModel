from django.db import models

# Create your models here.


#we create own user model and inherit from the django's user model originally

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length = 200, null = True)
    email = models.EmailField(unique = True) #if it s not unique - login can not be possible
    bio = models.TextField(null = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []