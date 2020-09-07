from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    artis = models.CharField(max_length=255)
    th = models.CharField(max_length=255)
    lirik = models.CharField(max_length=255)
    link  = models.CharField(max_length=255)

class Movie(models.Model):
    title = models.TextField(default='')
    gen   = models.TextField(default='')
    rate  = models.TextField(default='')
    years = models.TextField(default='')
    des   = models.TextField(default='')