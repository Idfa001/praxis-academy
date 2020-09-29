from django.forms import ModelForm

from . import models


class penjualan1f(ModelForm):
    class Meta:
        model = models.penjualan1m
        exclude = [ 'saldo_awal' ]

class saldoawalf(ModelForm):
    class Meta:
        model = models.saldoawalm
        exclude = [ ]

class penjualan2f(ModelForm):
    class Meta:
        model = models.penjualan2m
        exclude = [ 'terima' ]

class penjualan3f(ModelForm):
    class Meta:
        model = models.penjualan3m
        exclude = [ 'terima' ]

class utangf(ModelForm):
    class Meta:
        model = models.utangm
        exclude = ['dibayar']

class pend_lainf(ModelForm):
    class Meta:
        model = models.pend_lainm
        exclude = [ 'terima' ]

class pem_tunaif(ModelForm):
    class Meta:
        model = models.pem_tunaim
        exclude = []

class pem_kreditf(ModelForm):
    class Meta:
        model = models.pem_kreditm
        exclude = [ 'dibayar1' ]

class pem_lainf(ModelForm):
    class Meta:
        model = models.pem_lainm
        exclude = [ 'dibayar2' ]

class pembayaran_biayaf(ModelForm):
    class Meta:
        model = models.pembayaran_biayam
        exclude = []

class pembayaran_lainf(ModelForm):
    class Meta:
        model = models.pembayaran_lainm
        exclude = [ 'dibayar3' ]

class barangf(ModelForm):
    class Meta:
        model = models.barangm
        exclude = []

