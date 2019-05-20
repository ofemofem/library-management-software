from .models import LibraryBranch

from rest_framework import viewsets
from .serializers import LibraryBranchSerializer


class LibraryBranchViewSet(viewsets.ModelViewSet):
    queryset = LibraryBranch.objects.all()
    serializer_class = LibraryBranchSerializer




