from django.db import models

# Create your models here.
class feedback(models.Model):
    email = models.EmailField()
    feedback = models.TextField(max_length=1000)

    def __str__(self):
        return self.email