from .models import LibraryBranch

from rest_framework import serializers


class LibraryBranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = LibraryBranch
        fields = ['name', 'address', 'phone_number']