from .models import Borrow
from rest_framework import status
from rest_framework import viewsets
from backend.custom.permissions import IsReader
from rest_framework.response import Response
from rest_framework.decorators import action

from books.models import Book
from books.serializers import BookDetailSerializer
from .serializers import BorrowSerializer, BorrowDetailSerializer


from datetime import datetime


class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

    def get_permissions(self):
        # can be self.action = ... if we want check methods like 'list', 'retrieve' etc.
        if self.request.method == 'POST':
            self.permission_classes = [IsReader, ]
        else:
            self.permission_classes = []
            self.serializer_class = BorrowDetailSerializer
        return super(BorrowViewSet, self).get_permissions()


    def create(self, request, *args, **kwargs):
        serializer = BorrowSerializer(data=request.data, context={'request': request})
        book = Book.objects.get(id=request.data['book'])
        serialized_book = BookDetailSerializer(book)

        if serializer.is_valid():

            if serialized_book.data['borrow_status']['is_borrowed'] == False:
                serializer.save()
                return Response(204)

            return Response({'message':'This book is borrowed'}, 400)

        return Response(serializer.errors, 400)

    @action(detail=True)
    def return_book(self, request, pk):
        try:
            borrow = self.get_object()
        except Borrow.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if borrow:
            borrow.is_returned = True
            borrow.returned_date = datetime.now()
            borrow.save()
            return Response({"message": "the book has been returned"})

    @action(detail=True)
    def penalty(self, request, pk):
        try:
            borrow = self.get_object()
        except Borrow.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if borrow:
            borrow.is_penalty = True
            borrow.save()
            return Response({"message": "the book was not back on time"})


