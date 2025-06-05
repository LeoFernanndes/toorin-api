from django.db import models


class Book(models.Model):
    title = models.CharField('Title', max_length=255)
    isbm = models.CharField('ISBM', max_length=100)
    author = models.CharField('Author', max_length=100)
    publisher = models.CharField('Publisher', max_length=100)
    edition = models.IntegerField('Edition')
    pages = models.IntegerField('Number of pages')
    language = models.CharField('Language', max_length=100)
    description = models.TextField('Description')
    price = models.DecimalField('Price', max_digits=7, decimal_places=2)
    publish_date = models.DateField('Publish Date')
