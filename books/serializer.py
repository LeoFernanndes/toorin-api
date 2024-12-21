from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        books_list = self.Meta.model.objects.filter(
            titulo=data['title'], isbm=data["isbm"], autor=data["author"], editora=data["publisher"],
            edicao=data["edition"], num_paginas=data["pages"], descricao=data["description"]
        )
        if books_list.count() > 0:
            raise serializers.ValidationError("Book already present on the database")        
        return data
