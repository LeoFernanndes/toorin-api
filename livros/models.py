from django.db import models

# Create your models here.
class Livro(models.Model):
    titulo = models.CharField('Título', max_length=100)
    isbm = models.CharField('ISBM', max_length=100)
    autor = models.CharField('Autor', max_length=100)
    editora = models.CharField('Editora', max_length=100)
    edicao = models.IntegerField('Edição')
    num_paginas = models.IntegerField('Número de páginas')
    descricao = models.CharField('Descrição', max_length=100)