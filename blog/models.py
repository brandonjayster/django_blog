from django.db import models

# Create your models here.
# class post (models.Model) creates table
# create column title body etc
class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

def __str__ (self):
    return self.title
