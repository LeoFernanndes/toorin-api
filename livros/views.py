from rest_framework import viewsets, generics
from livros.models import Livro
from livros.serializer import LivroSerializer
from rest_framework.response import Response
from rest_framework import status


class LivrosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os livros"""
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    def create(self, request):
        #Set your serializer
        serializer = LivroSerializer(data=request.data)
        books_list = Livro.objects.all()

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
