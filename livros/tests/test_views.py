import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Livro
from ..serializer import LivroSerializer
from ..views import LivrosViewSet
from rest_framework.test import APIRequestFactory, RequestsClient

# initialize the APIClient app
client = Client()

class GetAllPuppiesTest(TestCase):
    """ Testar get de todos os livros """

    def setUp(self):
        Livro.objects.create(
           titulo="O Seminarista", isbm="102030",  autor="José de Alencar",  editora="Leia", edicao=10, num_paginas=230, descricao="Romance histórico, Bucolismo"
        )
        Livro.objects.create(
           titulo="Dom Quixote", isbm="102031",  autor="Migel de Cervantes",  editora="Leia", edicao=19, num_paginas=430, descricao="Aventura, Fantasia"
        )
    
    
    def test_get_all_books(self):
        # get API response
        response = self.client.get('/livros/', follow=True)

        # get data from db
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_post_one_complete_book(self):  
        data = {
            "titulo": "Biblia",
            "isbm": "10302014",
            "autor": "Vários",
            "editora": "Vida",
            "edicao": "5",
            "num_paginas": 1500,
            "descricao": "Religiososo"
        }

        response = self.client.post('/livros/', data=data, content=json, follow=True)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Livro.objects.get(titulo='Biblia').titulo, "Biblia")

    def test_post_one_repeated_book(self):
        data = {
            "titulo": "O Seminarista",
            "isbm": "102030",
            "autor": "José de Alencar",
            "editora": "Leia",
            "edicao": 10,
            "num_paginas": 230,
            "descricao": "Romance histórico, Bucolismo"
        }

        response = self.client.post('/livros/', data=data, content=json, follow=True)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  


    def test_post_one_incomplete_book(self):

        data = {
            "titulo": "As Valquírias",
            "isbm": "12503602",
            "autor": "Paulo Coelo",
            "editora": "Paulo Coelho",
            "edicao": "2",
            "num_paginas": 1500,
            "descricao": ""
        }

        response = self.client.post('/livros/', data=data, content=json, follow=True)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

