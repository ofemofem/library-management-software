from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_reader = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)

