from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator


class Group(models.Model):
    title = models.CharField(max_length=100)
    introduce = models.TextField(max_length=400)
    place = models.CharField(max_length=200)
    meeting_date = models.DateTimeField()
    number = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    like_user = models.ManyToManyField(get_user_model(), related_name="like_group")
    image = models.ImageField()
    closed = models.BooleanField(default=False)
