from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        books_list = self.Meta.model.objects.filter(
            title=data['title'], isbm=data["isbm"], author=data["author"], publisher=data["publisher"],
            edition=data["edition"], pages=data["pages"], description=data["description"]
        )
        if books_list.count() > 0:
            raise serializers.ValidationError("Book already present on the database")        
        return data
