from django.db import models
from django.contrib.auth import get_user_model


class Group(models.Model):
    title = models.CharField(max_length=200)
    introduce = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    detail_place = models.CharField(max_length=200,default="모임장소")
    meeting_date = models.DateField()
    number = models.PositiveIntegerField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    like_user = models.ManyToManyField(get_user_model(), related_name="like_group")
    image = models.ImageField()
    closed = models.BooleanField(default=False)


    

