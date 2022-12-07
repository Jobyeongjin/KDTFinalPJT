from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=20)
    interest = models.CharField(null=False, default="", max_length=20)
    profile_image = ProcessedImageField(
        upload_to="media/",
        blank=True,
        processors=[ResizeToFill(200, 200)],
        format="JPEG",
        options={"quality": 70},
    )
    age = models.PositiveIntegerField(default=0)
    status_message = models.TextField()
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )

    def user_image(self):
        if self.profile_image and hasattr(self.profile_image, "url"):
            return self.profile_image.url
        else:
            return "/static/image/no_profile.png"
