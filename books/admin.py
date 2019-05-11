from django.contrib import admin
from .models import Book, BookAuthor, BookCategory, LibraryBranch, Hire


admin.site.register(Book)
admin.site.register(BookAuthor)
admin.site.register(BookCategory)
admin.site.register(LibraryBranch)
admin.site.register(Hire)
