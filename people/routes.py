from rest_framework import routers
from django.urls import path

from people.viewsets import UserViewSet
from people.views import ChangeUserPasswordView


router = routers.SimpleRouter()
router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    path('users/<int:pk>/change_user_password/', ChangeUserPasswordView.as_view(), name='change-user-password'),
]
urlpatterns += router.urls
