from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from people.models import User
from people.serializers import UserCreateSerializer, UserRetrieveSerializer, UserUpdateSerializer
from people.permissions import UserPermission


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [UserPermission]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        if self.action == "update":
            return UserUpdateSerializer
        else:
            return UserRetrieveSerializer
