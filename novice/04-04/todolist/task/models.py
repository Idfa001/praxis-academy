from django.db import models

# Create your models here.
class Task(models.Model): #pakaian
    nama = models.CharField(max_length=255)
    ukuran = models.CharField(max_length=255)
    stok = models.CharField(max_length=255)
    deskripsi = models.CharField(max_length=255)
    harga = models.CharField(max_length=255)
    
class Movie(models.Model): #makanan
    nama = models.CharField(max_length=255)
    stok = models.CharField(max_length=255)
    kedaluarsa  = models.CharField(max_length=255)
    deskripsi = models.CharField(max_length=255)
    harga = models.CharField(max_length=255)

class Comic(models.Model): #elektronik
    nama = models.CharField(max_length=255)
    stok = models.CharField(max_length=255)
    deskripsi = models.CharField(max_length=255)
    harga = models.CharField(max_length=255)
