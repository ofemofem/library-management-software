from .models import Borrow

from rest_framework import serializers


class BorrowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Borrow
        fields = ['borrow_date', 'return_date', 'penalty_amount', 'is_penalty', 'book', 'borrower']


