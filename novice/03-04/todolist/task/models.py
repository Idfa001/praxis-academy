from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.TextField(default='')
    genre = models.TextField(default='')
    artis = models.TextField(default='')
    th = models.TextField(default='')
    lirik = models.TextField(default='')
    link  = models.TextField(default='')

class Movie(models.Model):
    title = models.TextField(default='')
    gen   = models.TextField(default='')
    rate  = models.TextField(default='')
    years = models.TextField(default='')
    des   = models.TextField(default='')