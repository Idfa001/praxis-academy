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
    title = models.CharField(max_length=255)
    gen   = models.CharField(max_length=255)
    rate  = models.CharField(max_length=255)
    years = models.CharField(max_length=255)
    des   = models.CharField(max_length=255)