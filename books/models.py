from django.db import models
from django.contrib.auth import get_user_model


class Book(models.Model):
    bookname = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    publication_year = models.CharField(max_length=100)
    bookcover = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

class Book_Review(models.Model):
    content = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_review = models.ManyToManyField(get_user_model(), related_name="like_review")

class Book_Review_Comment(models.Model):
    content = models.TextField()
    created_at = models.DateField()