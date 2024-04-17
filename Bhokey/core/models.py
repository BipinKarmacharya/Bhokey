from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='default_user.png')
    location = models.CharField(max_length=100, blank=True)

    def _str_(self):
        return self.user.username
    

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    location = models.TextField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now)
    Status_Choices=[
        ('open','Open'),
        ('reserved','Reserved'),
        ('provided','Provided')
    ]
    status = models.CharField(max_length=20, choices=Status_Choices, default='open')


    def __str__(self):
        return self.user


class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
    