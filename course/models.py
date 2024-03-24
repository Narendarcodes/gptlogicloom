from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Answers(models.Model):
    topic = models.CharField(max_length=10, primary_key=True)
    que1 = models.CharField(max_length=2)
    que2 = models.CharField(max_length=2)

    
    
    def __str__(self):
        return self.topic
class userprogress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    completed_topic = models.ManyToManyField(Answers)    
     
