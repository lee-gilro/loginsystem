from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from django.urls import reverse
from datetime import datetime

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()
    address = models.CharField(max_length=200, default= "None")
    private_key = models.CharField(max_length=200, default= "None")


    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

class Point(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.FloatField(default=0)
    token_lock = models.FloatField(default=0)
    remaining_days = models.IntegerField()
    memo = models.TextField()

    def __str__(self):
        return self.user.username

class PointHistory(models.Model):
    user = models.ForeignKey(User, null= True, on_delete=models.CASCADE)
    token = models.FloatField(default=0)
    send_dt = models.DateTimeField(auto_created=True)
    def __str__(self):
        return self.user.username

class Announcement(models.Model):
    title = models.CharField(max_length= 100)
    date = models.DateTimeField()
    content = models.TextField()
    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length= 200)
    answer = models.TextField()
    def __str__(self) -> str:
        return self.question


