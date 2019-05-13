from .models import Borrow

from rest_framework import viewsets
from .serializers import BorrowSerializer
from backend.custom.permissions import IsReader


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
