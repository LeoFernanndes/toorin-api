from django.db import models


class Book(models.Model):
    title = models.CharField('Title', max_length=100)
    isbm = models.CharField('ISBM', max_length=100)
    author = models.CharField('Author', max_length=100)
    publisher = models.CharField('Publisher', max_length=100)
    edition = models.IntegerField('Edition')
    pages = models.IntegerField('Number of pages')
    description = models.CharField('Description', max_length=100)
