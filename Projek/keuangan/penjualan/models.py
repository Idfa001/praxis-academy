from django.db import models

# Create your models here.
class Penjualan(models.Model):
	tanggal = models.DateField(default='tanggal', max_length= 255)
	keterangan = models.CharField(default='Keterangan', max_length= 255)
	jumlah = models.IntegerField()
	catatan = models.CharField(default='Catatan', max_length= 255)