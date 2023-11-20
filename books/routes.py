from rest_framework import routers

from books.viewsets import BookViewSet

router = routers.SimpleRouter()
router.register(r"", BookViewSet, basename="book")

urlpatterns = []
urlpatterns += router.urls