from rest_framework import routers

from people.viewsets import UserViewSet

router = routers.SimpleRouter()
router.register(r"users", UserViewSet, basename="user")

urlpatterns = []
urlpatterns += router.urls
