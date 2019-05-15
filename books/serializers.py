from .models import Book, BookCategory, BookAuthor
from borrow.models import Borrow
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
    library_branch = serializers.StringRelatedField()
    borrow_status = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'pages_count',
            'publish_year',
            'library_branch',
            'book_categories',
            'author',
            'borrow_status'
        ]

    def get_borrow_status(self, obj):
        borrow = Borrow.objects.filter(book=obj.id, is_returned=False)
        if not borrow:
            return 'available'
        return 'on_borrow'



