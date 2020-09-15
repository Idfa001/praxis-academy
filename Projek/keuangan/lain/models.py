from django.db import models
from datetime import datetime

class Lain(models.Model):
  tanggal_transaksi = models.DateField(
        auto_now_add=True
    )
  keterangan = models.CharField(max_length=255)
  kas = models.IntegerField(default=0)
  piutang = models.IntegerField()
  catatan = models.CharField(max_length=255)
  def tanggal_transaksi_f(self):
    return self.tanggal_transaksi.strftime("%d %b %Y ")

