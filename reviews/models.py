from django.db import models
from django.contrib.auth import get_user_model
from books.models import Book
from taggit.managers import TaggableManager
from django.utils import timezone
from datetime import datetime, timedelta


class Book_Review(models.Model):
    content = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    color = models.CharField(max_length=7, default="#FFFFFF")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    like_user = models.ManyToManyField(get_user_model(), related_name="like_review")
    bookId = models.ForeignKey(Book, on_delete=models.CASCADE)
    tags = TaggableManager(blank=True)

    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return "방금 전"
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + "분 전"
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + "시간 전"
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + "일 전"
        else:
            return False


class Book_Review_Comment(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book_review = models.ForeignKey(Book_Review, on_delete=models.CASCADE)
