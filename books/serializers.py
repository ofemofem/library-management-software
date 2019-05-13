from .models import Book, BookCategory, BookAuthor

from rest_framework import serializers


class BookCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = BookCategory
        fields = ['id', 'name']


class BookAuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookAuthor
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    book_categories = serializers.StringRelatedField(many=True)
    borrow_status = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            'title',
            'pages_count',
            'publish_year',
            'library_branch',
            'book_categories',
            'author',
            'borrow_status'
        ]




