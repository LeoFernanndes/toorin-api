from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework import pagination

from books.models import Book
from books.serializer import BookSerializer


class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = CustomPageNumberPagination

    @method_decorator(cache_page(60, key_prefix="books-key-cache"))
    def list(self, request, *args, **kwargs):
        keys = cache
        return super().list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # TODO: find ways of generalizing cache invalidation
        keys = cache.keys("*")
        keys_to_be_deleted = [k for k in keys if "books-key-cache" in k]
        cache.delete_many(keys_to_be_deleted)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # TODO: find ways of generalizing cache invalidation
        keys = cache.keys("*")
        keys_to_be_deleted = [k for k in keys if "books-key-cache" in k]
        cache.delete_many(keys_to_be_deleted)
        return super().destroy(request, *args, **kwargs)
