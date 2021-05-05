 
from rest_framework import viewsets, generics
from livros.models import Livro
from livros.serializer import LivroSerializer

class LivrosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os livros"""
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer