from django.db import models

# Create your models here.
class Task(models.Model):
    judul = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    artis = models.CharField(max_length=255)
    tahun = models.CharField(max_length=255)
    lirik = models.CharField(max_length=255)
    link  = models.CharField(max_length=255)

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    rate  = models.CharField(max_length=255)
    years = models.CharField(max_length=255)
    deskripsi = models.CharField(max_length=255)

class Comic(models.Model):
    judul = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    update = models.CharField(max_length=255)