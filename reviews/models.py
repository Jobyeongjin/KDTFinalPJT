from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Book_Review(models.Model):
    content = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    like_user = models.ManyToManyField(get_user_model(), related_name="like_review")

class Book_Review_Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book_review = models.ForeignKey(Book_Review, on_delete=models.CASCADE)