from django.db import models

# Create your models here.
class Answers(models.Model):
    topic = models.CharField(max_length=10, primary_key=True)
    que1 = models.CharField(max_length=2)
    que2 = models.CharField(max_length=2)
    submission = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.topic
     
     