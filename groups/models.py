from django.db import models
from django.contrib.auth import get_user_model


class Group(models.Model):
    title = models.CharField(max_length=200)
    introduce = models.TextField()
    place = models.TextField()
    meeting_date = models.DateField()
    number = models.IntegerField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    like_user = models.ManyToManyField(get_user_model(), related_name="like_group")
    image = models.ImageField()
    closed = models.BooleanField(default=False)

    X = models.CharField(max_length=20, null=True)
    Y = models.CharField(max_length=20, null=True)

