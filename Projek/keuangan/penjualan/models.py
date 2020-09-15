from django.db import models

# Create your models here.
class Penjualan(models.Model):
	tanggal = models.DateField(auto_now_add=True)
	keterangan = models.CharField(default='Keterangan', max_length= 255)
	jumlah = models.IntegerField()
	catatan = models.CharField(default='Catatan', max_length= 255)
	
	def tanggal_f(self):
		return self.tanggal.strftime("%d %b %Y ")


