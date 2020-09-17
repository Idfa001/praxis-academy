from django.db import models

class barangm(models.Model):
    barang = models.CharField(max_length=200)
    harga_beli = models.IntegerField(default=0)
    harga_jual = models.IntegerField(default=0)

    def __str__(self):
        return self.barang


class penjualan1m(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    barang = models.ForeignKey(barangm, on_delete = models.DO_NOTHING)
    kuantitas = models.IntegerField(default=0)
    catatan = models.TextField(default="")

    def total(self):
        return self.barang.harga_jual * self.kuantitas

class penjualan2m(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    barang = models.ForeignKey(barangm, on_delete = models.DO_NOTHING)
    kuantitas = models.IntegerField(default=0)
    catatan = models.TextField(default="")


    def total(self):
        return self.barang.harga_jual * self.kuantitas

class penjualan3m(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=200)
    kas = models.IntegerField(default=0)
    piutang = models.IntegerField(default=0)
    catatan = models.TextField(default="")

    def jumlah(self):
        return self.kas 
    
    def jumlah2(self):
        return self.piutang

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


    

