from django.db import models

class penjualan1m(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    barang = models.CharField(max_length=200)
    kuantitas = models.IntegerField(default=0)
    jumlah = models.DecimalField(max_digits=10, decimal_places=2)
    catatan = models.TextField(default="")

class penjualan2m(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    barang = models.CharField(max_length=200)
    kuantitas = models.IntegerField(default=0)
    jumlah = models.DecimalField(max_digits=10, decimal_places=2)
    catatan = models.TextField(default="")

class penjualan3m(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=200)
    kas = models.IntegerField(default=0)
    piutang = models.IntegerField(default=0)
    catatan = models.TextField(default="")

class utangm(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=200)
    jumlah = models.DecimalField(max_digits=10, decimal_places=2)
    catatan = models.TextField(default="")

class pend_lainm(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=200)
    jumlah = models.DecimalField(max_digits=10, decimal_places=2)
    catatan = models.TextField(default="")

class pem_tunaim(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=200)
    jumlah = models.DecimalField(max_digits=10, decimal_places=2)
    catatan = models.TextField(default="")

class pem_kreditm(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=200)
    jumlah = models.DecimalField(max_digits=10, decimal_places=2)
    catatan = models.TextField(default="")

class pem_lainm(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=200)
    jumlah = models.DecimalField(max_digits=10, decimal_places=2)
    catatan = models.TextField(default="")

class pembayaran_biayam(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=200)
    dibayar = models.DecimalField(max_digits=10, decimal_places=2)
    catatan = models.TextField(default="")

class pembayaran_lainm(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=200)
    utang = models.DecimalField(max_digits=10, decimal_places=2)
    dibayar = models.DecimalField(max_digits=10, decimal_places=2)
    catatan = models.TextField(default="")

class barangm(models.Model):
    barang = models.CharField(max_length=200)
    harga_beli = models.DecimalField(max_digits=10, decimal_places=2)
    harga_jual = models.DecimalField(max_digits=10, decimal_places=2)


