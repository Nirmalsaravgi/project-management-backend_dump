from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256, unique=True)
    password = models.CharField(max_length=256)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
