from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

from people.models import User
from people.serializers import CustomTokenObtainPairSerializer, ChangeUserPasswordSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    # TODO: implement some token rotatino logic to revoke user refresh tokens
    serializer_class = CustomTokenObtainPairSerializer


class ChangeUserPasswordView(mixins.UpdateModelMixin, GenericAPIView):
    queryset = User.objects.all()
    serializer_class = ChangeUserPasswordSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
