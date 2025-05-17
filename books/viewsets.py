from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny

from books.models import Book
from books.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework import status


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
