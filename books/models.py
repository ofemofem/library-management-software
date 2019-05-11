from django.db import models
from django.conf import settings

class LibraryBranch(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class BookCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    pages_count = models.IntegerField()
    publish_year = models.IntegerField()

    library_branch = models.OneToOneField(LibraryBranch, on_delete=models.CASCADE, null=True, blank=True)
    book_categories = models.ManyToManyField(BookCategory, blank=True)

    def __str__(self):
        return self.title


class BookAuthor(models.Model):
    name = models.CharField(max_length=255)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='BookAuthor')

    def __str__(self):
        return self.name


class Hire(models.Model):
    hire_date = models.TimeField()
    return_date = models.TimeField()
    penalty_amount = models.IntegerField()
    is_penalty = models.BooleanField(default=False)
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    hired_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

