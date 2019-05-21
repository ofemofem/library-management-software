from books.models import BookCategory
from rest_framework import viewsets
from books.serializers import BookCategorySerializer

from library_branch.models import LibraryBranch
from library_branch.serializers import LibraryBranchSerializer

from rest_framework.response import Response


class DictionariesViewSet(viewsets.ViewSet):

    def list(self, request):
        branches = LibraryBranch.objects.all()
        categories = BookCategory.objects.all()

        serializer_branches = LibraryBranchSerializer(branches, many=True)
        serializer_categories = BookCategorySerializer(categories, many=True)

        response = {
            'library_branches': serializer_branches.data,
            'book_categories': serializer_categories.data,
        }

        return Response(response)