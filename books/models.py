from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


class Book(models.Model):
    bookname = models.CharField(max_length=1000)
    authors = models.CharField(max_length=1000)
    publisher = models.CharField(max_length=1000)
    publication_year = models.CharField(max_length=1000)
    class_nm = models.CharField(max_length=2000)
    bookcover = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="books")
