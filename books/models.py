from django.db import models
from django.contrib.auth import get_user_model


class Book(models.Model):
    bookname = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    publication_year = models.CharField(max_length=100)
    bookcover = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    like_user = models.ManyToManyField(get_user_model(), related_name="like_book")

class Book_Review(models.Model):
    content = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    like_user = models.ManyToManyField(get_user_model(), related_name="like_review")

class Book_Review_Comment(models.Model):
    content = models.TextField()
    created_at = models.DateField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    review = models.ForeignKey(Book_Review, on_delete=models.CASCADE)