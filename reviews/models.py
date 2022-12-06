from django.db import models
from django.contrib.auth import get_user_model
from books.models import Book


class Book_Review(models.Model):
    content = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    like_user = models.ManyToManyField(get_user_model(), related_name="like_review")
    bookId = models.ForeignKey(Book, on_delete=models.CASCADE)


class Book_Review_Comment(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book_review = models.ForeignKey(Book_Review, on_delete=models.CASCADE)
