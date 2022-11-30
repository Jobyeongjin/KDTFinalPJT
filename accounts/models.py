from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=20)
    interest = models.CharField(null=False,default='' , max_length=20)
    profile_image = ProcessedImageField(
        upload_to="media/",
        blank=True,
        processors=[ResizeToFill(100, 100)],
        format="JPEG",
        options={"quality": 60},
    )
    age = models.IntegerField(default=0)
    status_message = models.TextField()
    following = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )
    
