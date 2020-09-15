from django.db import models

# Create your models here.
class Biaya(models.Model):
	tanggal = models.DateField(default='tanggal', max_length= 255)
	keterangan = models.CharField(default='Keterangan', max_length= 255)
	bayar = models.IntegerField()
	hutang = models.IntegerField()
	catatan = models.CharField(default='Catatan', max_length= 255)