from .models import Book, BookCategory, BookAuthor, LibraryBranch, Hire

from rest_framework import viewsets
from .serializers import (
    BookSerializer,
    BookCategorySerializer,
    BookAuthorSerializer,
    LibraryBranchSerializer,
    HireSerializer
)
from backend.permissions import IsLibrarian


class LibraryBranchViewSet(viewsets.ModelViewSet):
    queryset = LibraryBranch.objects.all()
    serializer_class = LibraryBranchSerializer


class BookCategoryViewSet(viewsets.ModelViewSet):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

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
