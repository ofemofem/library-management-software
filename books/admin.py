from django.contrib import admin
from .models import Book, BookAuthor, BookCategory


admin.site.register(Book)
admin.site.register(BookAuthor)
admin.site.register(BookCategory)
