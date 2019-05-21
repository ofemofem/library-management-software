from .models import Book, BookCategory, BookAuthor

from rest_framework import viewsets
from .serializers import (
    BookSerializer,
    BookCategorySerializer,
    BookAuthorSerializer,
    BookDetailSerializer,
)
from backend.custom.permissions import IsLibrarian

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend



class BookCategoryViewSet(viewsets.ModelViewSet):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('book_categories', 'publish_year', 'library_branch')
    search_fields = ['title', 'author__name']
    ordering_fields = ['created_at']

    def get_permissions(self):
        # can be self.action = ... if we want check methods like 'list', 'retrieve' etc.
        if self.request.method != 'GET':
            self.permission_classes = [IsLibrarian, ]
        else:
            self.permission_classes = []
            self.serializer_class = BookDetailSerializer

        return super(BookViewSet, self).get_permissions()


class BookAuthorViewSet(viewsets.ModelViewSet):
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer




