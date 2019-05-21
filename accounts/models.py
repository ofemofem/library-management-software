from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=254, null=False)
    last_name = models.CharField(max_length=254, null=False)
    is_reader = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)



