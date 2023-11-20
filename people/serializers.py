
import traceback
from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from people.models import User


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = "__all__"


class UserRetrieveSerializer(UserSerializer):
    class Meta:
        model = User
        exclude = ['password', 'groups', 'user_permissions']


class UserCreateSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    def to_representation(self, instance):
        return UserRetrieveSerializer().to_representation(instance)


class UserUpdateSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    user = serializers.SerializerMethodField()

    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        user_data = UserRetrieveSerializer().to_representation(self.user)
        data.update({"user": user_data})
        return data
