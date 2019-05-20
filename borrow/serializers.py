from .models import Borrow
from books.serializers import BookSerializer

from rest_framework import serializers

from accounts.serializers import UserSerializer


class BorrowSerializer(serializers.ModelSerializer):
    borrower = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Borrow
        fields = '__all__'


class BorrowDetailSerializer(serializers.ModelSerializer):

    borrower = UserSerializer(many=False, read_only=True)
    book = BookSerializer(many=False, read_only=True)

    class Meta:
        model = Borrow
        fields = [
            'id',
            'borrow_date',
            'return_date',
            'returned_date',
            'penalty_amount',
            'is_penalty',
            'book',
            'borrower',
            'is_returned'
        ]
        # depth = 1

