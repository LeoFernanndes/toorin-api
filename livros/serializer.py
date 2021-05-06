from rest_framework import serializers
from .models import Livro

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
    
    # titulo = serializers.CharField()
    # isbm = serializers.CharField()
    # autor = serializers.CharField()
    # editora = serializers.CharField()
    # edicao = serializers.IntegerField()
    # num_paginas = serializers.IntegerField()
    # descricao = serializers.CharField()

    def validate(self, data):
        
        # books_list = Livro.objects.filter(titulo=data.titulo, isbm=data.isbm, autor=data.autor, editora=data.autor, edicao=data.edicao, num_paginas=data.num_paginas, descricao=data.descricao)
        books_list = Livro.objects.filter(
            titulo=data['titulo'], isbm=data["isbm"], autor=data["autor"], editora=data["editora"],
            edicao=data["edicao"], num_paginas=data["num_paginas"], descricao=data["descricao"]
        )

        if len(list(books_list)) > 0:
            raise serializers.ValidationError("Book already present on the database")        
        return data
