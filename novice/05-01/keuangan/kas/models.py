from django.db import models

class Penjualan(models.Model):
  tanggal_transaksi = models.DateTimeField(null=True, blank=True)
  nama_barang = models.CharField(max_length=255)
  jumlah_barang = models.IntegerField(default=0)
  harga = models.DecimalField(default=0,max_digits=6, decimal_places=2)