from rest_framework import serializers
from rest_framework.validators import UniqueValidator
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
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    def validate_email(self, email):
        #TODO: create a common to validate emails
        return email

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


class ChangeUserPasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)
    new_password = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)

    class Meta:
        model = User
        fields = ['old_password', 'new_password']

    def validate_old_password(self, old_password):
        if not self.instance.check_password(old_password):
            raise serializers.ValidationError('Current password is incorrect')
        return old_password

    def validate_new_password(self, new_password):
        # implement some  business rules for password validation 
        return new_password

    def save(self, **kwargs):
        # reimplements .save() with minimal changes to set new password 
        assert hasattr(self, '_errors'), (
            'You must call `.is_valid()` before calling `.save()`.'
        )

        assert not self.errors, (
            'You cannot call `.save()` on a serializer with invalid data.'
        )

        # Guard against incorrect use of `serializer.save(commit=False)`
        assert 'commit' not in kwargs, (
            "'commit' is not a valid keyword argument to the 'save()' method. "
            "If you need to access data before committing to the database then "
            "inspect 'serializer.validated_data' instead. "
            "You can also pass additional keyword arguments to 'save()' if you "
            "need to set extra attributes on the saved model instance. "
            "For example: 'serializer.save(owner=request.user)'.'"
        )

        assert not hasattr(self, '_data'), (
            "You cannot call `.save()` after accessing `serializer.data`."
            "If you need to access data before committing to the database then "
            "inspect 'serializer.validated_data' instead. "
        )

        validated_data = {**self.validated_data, **kwargs}
        self.instance.set_password(validated_data['new_password'])
        self.instance.save()
        return self.instance

    def to_representation(self, instance):
        return {'detail': 'Successfuly changed password'}