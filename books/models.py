from django.db import models


# class LibraryBranch(models.Model):
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     phone_number = models.IntegerField()
#
#     def __str__(self):
#         return self.name
#
#
# class BookCategory(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    pages_count = models.IntegerField()
    publish_year = models.IntegerField()

    # library_branch = models.OneToOneField(LibraryBranch, on_delete=models.CASCADE)
    # book_categories = models.ManyToManyField(BookCategory)

    def __str__(self):
        return self.title


# class BookAuthor(models.Model):
#     name = models.CharField(max_length=255)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name
#
#
# class Hire(models.Model):
#     hire_date = models.TimeField(auto_now_add=True)
#     return_date = models.TimeField()
#     penalty_amount = models.IntegerField(default=0)
#     is_penalty = models.BooleanField(default=False)
#     book = models.OneToOneField(Book, on_delete=models.CASCADE)


