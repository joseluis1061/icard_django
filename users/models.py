from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 200)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    is_active = models.BooleanField()
    is_staff = models.BooleanField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []