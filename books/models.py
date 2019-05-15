from django.db import models

from library_branch.models import LibraryBranch


class BookCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class BookAuthor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    pages_count = models.IntegerField()
    publish_year = models.IntegerField()

    library_branch = models.ForeignKey(LibraryBranch, on_delete=models.CASCADE, null=True, blank=True)
    book_categories = models.ManyToManyField(BookCategory, blank=True)
    author = models.ForeignKey(BookAuthor, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
