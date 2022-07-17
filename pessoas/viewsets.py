from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from pessoas.models import User
from pessoas.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]
