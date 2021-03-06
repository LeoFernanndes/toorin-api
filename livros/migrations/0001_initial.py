# Generated by Django 3.2.1 on 2021-05-04 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('isbm', models.CharField(max_length=100, verbose_name='ISBM')),
                ('autor', models.CharField(max_length=100, verbose_name='Autor')),
                ('editora', models.CharField(max_length=100, verbose_name='Editora')),
                ('edicao', models.IntegerField(verbose_name='Edição')),
                ('num_paginas', models.IntegerField(verbose_name='Número de páginas')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
            ],
        ),
    ]
