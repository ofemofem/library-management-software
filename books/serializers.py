from .models import Book, BookCategory, BookAuthor, LibraryBranch, Hire

from rest_framework import serializers


class LibraryBranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = LibraryBranch
        fields = ['name', 'address', 'phone_number']


class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['title', 'pages_count', 'publish_year', 'library_branch', 'book_categories']


class BookAuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookAuthor
        fields = ['name', 'book']


class HireSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hire
        fields = ['hire_date', 'return_date', 'penalty_amount', 'is_penalty', 'book', 'hired_by']


