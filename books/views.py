from .models import Book, BookCategory, BookAuthor, LibraryBranch, Hire

from rest_framework import viewsets
from .serializers import (
    BookSerializer,
    BookCategorySerializer,
    BookAuthorSerializer,
    LibraryBranchSerializer,
    HireSerializer
)
from backend.custom.permissions import IsLibrarian, IsReader

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class LibraryBranchViewSet(viewsets.ModelViewSet):
    queryset = LibraryBranch.objects.all()
    serializer_class = LibraryBranchSerializer


class BookCategoryViewSet(viewsets.ModelViewSet):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('book_categories', 'publish_year')
    search_fields = ['title', 'author__name']

    def get_permissions(self):
        # can be self.action = ... if we want check methods like 'list', 'retrieve' etc.
        if self.request.method != 'GET':
            self.permission_classes = [IsLibrarian, ]
        else:
            self.permission_classes = []

        return super(BookViewSet, self).get_permissions()


class BookAuthorViewSet(viewsets.ModelViewSet):
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer


class HireViewSet(viewsets.ModelViewSet):
    queryset = Hire.objects.all()
    serializer_class = HireSerializer

    def get_permissions(self):
        # can be self.action = ... if we want check methods like 'list', 'retrieve' etc.
        if self.request.method == 'POST':
            self.permission_classes = [IsReader, ]
        else:
            self.permission_classes = []

        return super(HireViewSet, self).get_permissions()
