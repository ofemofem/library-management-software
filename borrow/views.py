from .models import Borrow
from books.models import Book
from rest_framework import status
from rest_framework import viewsets
from .serializers import BorrowSerializer
from backend.custom.permissions import IsReader
from rest_framework.response import Response
from rest_framework.decorators import action


class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

    def get_permissions(self):
        # can be self.action = ... if we want check methods like 'list', 'retrieve' etc.
        if self.request.method == 'POST':
            self.permission_classes = [IsReader, ]
        else:
            self.permission_classes = []

        return super(BorrowViewSet, self).get_permissions()

    @action(detail=True)
    def return_book(self, request, pk):
        try:
            borrow = self.get_object()
        except Borrow.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if borrow:
            borrow.is_returned = True
            borrow.save()
            return Response({"message": "the book has been returned"})



