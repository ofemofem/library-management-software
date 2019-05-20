from .models import Book, BookCategory, BookAuthor
from borrow.models import Borrow

from rest_framework import serializers

from library_branch.serializers import LibraryBranchSerializer


class BookCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = BookCategory
        fields = ['id', 'name']


class BookAuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookAuthor
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):

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
        ]


class BookDetailSerializer(serializers.ModelSerializer):

    author = BookAuthorSerializer(many=False, read_only=True)
    book_categories = BookCategorySerializer(many=True, read_only=True)
    library_branch = LibraryBranchSerializer(many=False, read_only=True)

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
        borrow = Borrow.objects.filter(book=obj.id, is_returned=False).first()
        serialized_borrow = BorrowSerializer(borrow)
        if not borrow:
            return {
                "is_borrowed": False,
                "return_date": None
            }
        return {
                "is_borrowed": True,
                "return_date": serialized_borrow.data['return_date']
            }


from borrow.serializers import BorrowSerializer
