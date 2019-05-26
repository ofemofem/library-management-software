from rest_framework import serializers
from borrow.models import Borrow
from .models import User

from datetime import datetime


class UserSerializer(serializers.ModelSerializer):
    is_blocked = serializers.SerializerMethodField()

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        exclude = ('password',)

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user

    def get_is_blocked(self, obj):
        try:
            borrow = Borrow.objects.filter(borrower=obj.id, is_returned=False)
        except Borrow.DoesNotExist:
            borrow = None

        if borrow:

            serialized_borrow = BorrowDetailSerializer(borrow, many=True)
            q = datetime.now()
            for i in serialized_borrow.data:
                if q > datetime.strptime(i['return_date'], "%Y-%m-%dT%H:%M:%S.%fZ"):
                    return True
            return False

        return False

from borrow.serializers import BorrowDetailSerializer


