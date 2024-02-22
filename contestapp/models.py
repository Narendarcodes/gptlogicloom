from django.db import models

class Contest(models.Model):
    title = models.CharField(max_length=100)    
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    hackerrank_link = models.URLField()

    def __str__(self):
        return self.title
