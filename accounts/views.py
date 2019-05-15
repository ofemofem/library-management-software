from rest_framework import viewsets

from .serializers import UserSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import list_route


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        return User.objects.filter(is_reader=True)

    @list_route(methods=['GET'], permission_classes=[IsAuthenticated])
    def me(self, request, *args, **kwargs):
        self.kwargs.update(pk=request.user.id)
        return self.retrieve(request, *args, **kwargs)








