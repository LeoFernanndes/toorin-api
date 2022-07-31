from rest_framework import routers

from livros.viewsets import LivrosViewSet

router = routers.SimpleRouter()
router.register(r"", LivrosViewSet, basename="livro")

urlpatterns = []
urlpatterns += router.urls