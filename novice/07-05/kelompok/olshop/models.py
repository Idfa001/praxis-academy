from django.db import models
from datetime import datetime

class barangm(models.Model):
    barang = models.CharField(max_length=200)
    harga_beli = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    harga_jual = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    
    def __str__(self):
        return self.barang
 
class saldoawalm(models.Model):
    saldo_awal = models.DecimalField(default=0, max_digits=10, decimal_places=0)

class penjualan1m(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    barang = models.ForeignKey(barangm, on_delete = models.DO_NOTHING)
    kuantitas = models.IntegerField(default=0)
    saldo_awal = models.DecimalField(default=0, max_digits=10, decimal_places=0)

    def tanggal1(self):
        return self.tanggal.strftime("%d/%m/%Y")

    def total(self):
        return self.barang.harga_jual * self.kuantitas

class penjualan2m(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    barang = models.ForeignKey(barangm, on_delete = models.DO_NOTHING)
    kuantitas = models.IntegerField(default=0)
    catatan = models.CharField(max_length=200)
    jatuh_tempo = models.DateField(default=datetime.now)
    terima = models.DecimalField(default=0, max_digits=10, decimal_places=0)

    def tanggal1(self):
        return self.tanggal.strftime("%d/%m/%Y")

    def tanggal2(self):
        return self.jatuh_tempo.strftime("%d/%m/%Y")

    def __str__(self):
        return self.terima
        
    def total(self):
        return self.barang.harga_jual * self.kuantitas

    def saldo(self):
        return self.total() - self.terima
    
    def jumlah3(self):
        return self.saldo

    def duda(self):
        return self.jatuh_tempo - datetime.now().date()
    
    def dadu(self):
        return self.duda().days


class penjualan3m(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=200)
    kas = models.IntegerField(default=0)
    piutang = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    catatan = models.CharField(max_length=200)
    terima = models.DecimalField(default=0, max_digits=10, decimal_places=0)

    def tanggal1(self):
        return self.tanggal.strftime("%d/%m/%Y")

    def jumlah(self):
        return self.kas 
    
    def jumlah2(self):
        return self.piutang

    def saldo(self):
        return self.piutang - self.terima

class utangm(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    catatan = models.CharField(max_length=200)
    jumlah = models.DecimalField(max_digits=10, decimal_places=0)
    # catatan = models.TextField(default="")
    dibayar = models.DecimalField(default=0, max_digits=10, decimal_places=0)

    def tanggal1(self):
        return self.tanggal.strftime("%d/%m/%Y")


    def jum_utang(self):
        return self.jumlah

    def saldo(self):
        return self.jumlah - self.dibayar

    def jumlah3(self):
        return self.saldo

class pend_lainm(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=200)
    jumlah = models.DecimalField(max_digits=10, decimal_places=0)
    piutang = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    catatan = models.CharField(max_length=200)
    terima  = models.DecimalField(max_digits=10, decimal_places=0, default=0)

    def tanggal1(self):
        return self.tanggal.strftime("%d/%m/%Y")

    def jum_pend(self):
        return self.jumlah

    def jum_pend1(self):
        return self.piutang

    def saldo(self):
        return self.piutang - self.terima

class pem_tunaim(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=200)
    jumlah = models.DecimalField(max_digits=10, decimal_places=0)
    catatan = models.CharField(max_length=200)

    def tanggal1(self):
        return self.tanggal.strftime("%d/%m/%Y")

    def jum_pem(self):
        return self.jumlah

class pem_kreditm(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=200)
    jumlah = models.DecimalField(max_digits=10, decimal_places=0)
    catatan = models.CharField(max_length=200)
    dibayar1 = models.DecimalField(default=0, max_digits=10, decimal_places=0)

    def tanggal1(self):
        return self.tanggal.strftime("%d/%m/%Y")

    def jum_pem(self):
        return self.jumlah

    def saldo(self):
        return self.jumlah - self.dibayar1


class pem_lainm(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=200)
    dibayar = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    utang = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    catatan = models.CharField(max_length=200)
    dibayar2 = models.DecimalField(default=0, max_digits=10, decimal_places=0)

    def tanggal1(self):
        return self.tanggal.strftime("%d/%m/%Y")

    def jum_pem(self):
        return self.dibayar

    def jum_pem1(self):
        return self.utang

    def saldo(self):
        return self.utang - self.dibayar2


class pembayaran_biayam(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=200)
    dibayar = models.DecimalField(max_digits=10, decimal_places=0)
    catatan = models.CharField(max_length=200)

    def tanggal1(self):
        return self.tanggal.strftime("%d/%m/%Y")

    def jum_pem(self):
        return self.dibayar

class pembayaran_lainm(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.CharField(max_length=200)
    dibayar = models.DecimalField(max_digits=10, decimal_places=0)
    utang = models.DecimalField(max_digits=10, decimal_places=0)
    catatan = models.CharField(max_length=200)
    dibayar3 = models.DecimalField(default=0, max_digits=10, decimal_places=0)

    def tanggal1(self):
        return self.tanggal.strftime("%d/%m/%Y")

    def jum1(self):
        return self.dibayar

    def jum2(self):
        return self.utang

    def saldo(self):
        return self.utang - self.dibayar3


    

