from django.db import models


class Book(models.Model):
    bookname = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    publication_year = models.CharField(max_length=100)
    bookcover = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
