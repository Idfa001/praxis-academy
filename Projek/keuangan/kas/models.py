from django.db import models
from datetime import datetime

class Penjualan(models.Model):
  tanggal_transaksi = models.DateField(
        auto_now_add=True
    )
  nama_barang = models.CharField(max_length=255)
  jumlah_barang = models.IntegerField(default=0)
  harga_satuan = models.IntegerField()
  def tanggal_transaksi_f(self):
    return self.tanggal_transaksi.strftime("%d %b %Y ")

