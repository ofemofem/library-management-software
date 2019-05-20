from .models import LibraryBranch

from rest_framework import serializers


class LibraryBranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = LibraryBranch
        fields = ['id', 'name', 'address', 'phone_number']
        exclude_when_nested = {'address', 'phone_number'}

    # def get_field_names(self, *args, **kwargs):
    #     field_names = super(LibraryBranchSerializer, self).get_field_names(*args, **kwargs)
    #     if self.parent:
    #         field_names = [i for i in field_names if i not in self.Meta.exclude_when_nested]
    #     return field_names