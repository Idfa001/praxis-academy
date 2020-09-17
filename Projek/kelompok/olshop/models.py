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
    terima = models.IntegerField(default=0)

    def __str__(self):
        return self.terima
        
    def total(self):
        return self.barang.harga_jual * self.kuantitas

    def saldo(self):
        return self.total() - self.terima
    
    def jumlah3(self):
        return self.saldo

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
    dibayar = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def jum_utang(self):
        return self.jumlah

    def saldo(self):
        return self.jumlah - self.dibayar

class pend_lainm(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=200)
    jumlah = models.DecimalField(max_digits=10, decimal_places=2)
    catatan = models.TextField(default="")

    def jum_pend(self):
        return self.jumlah

class pem_tunaim(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=200)
    jumlah = models.DecimalField(max_digits=10, decimal_places=2)
    catatan = models.TextField(default="")

    def jum_pem(self):
        return self.jumlah

class pem_kreditm(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=200)
    jumlah = models.DecimalField(max_digits=10, decimal_places=2)
    catatan = models.TextField(default="")

    def jum_pem(self):
        return self.jumlah

class pem_lainm(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=200)
    dibayar = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    utang = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    catatan = models.TextField(default="")

    def jum_pem(self):
        return self.dibayar


    def jum_pem1(self):
        return self.utang

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


    

