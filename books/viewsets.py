from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny

from books.models import Book
from books.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework import status


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [AllowAny]

    # reimplementação do método create para que as validações do serializer passem a ser consideradas
    # def create(self, request):
    #     #Set your serializer
    #     serializer = BookSerializer(data=request.data)
    #     books_list = Book.objects.all()
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
