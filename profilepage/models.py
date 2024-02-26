# models.py

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30)
    hackerrank_id = models.CharField(max_length=20)
    c1progress = models.FloatField(default='0')
    c2progress = models.FloatField(default='0')
    name = models.CharField(max_length=50)
    imguploadlimit = models.PositiveSmallIntegerField(default='10')
    image = models.ImageField(upload_to='profile_images/', default='profile_images/default.jpg')

    def __str__(self):
        return self.user.username
