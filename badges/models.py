# badges/models.py

from django.contrib.auth.models import User
from django.db import models

class Badge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='badges/')

    def __str__(self):
        return self.name

class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    progress = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Progress"

    def award_badges(self):
        current_badges = self.user.badges.all().count()
        new_badges = self.progress // 10 - current_badges
        if new_badges > 0:
            latest_badges = Badge.objects.order_by('-id')[:new_badges]
            self.user.badges.add(*latest_badges)
