from django.shortcuts import render, redirect
from django.db.models import Sum
from . import forms
from . import models


def halamandepan(req):
    return render(req, 'hal1/index1.html')

def penjualan(req):
    return render(req, 'uangmasuk/index2.html')

def penjualan_tunai(req):
    penjualan1 = models.penjualan1m.objects.all()
    total = 0
    for p in penjualan1:
      total += p.total()
    return render(req, 'penjualan/index3.html', {
        'data': penjualan1,
        'total': total,
    })

def penjualan_kredit(req):
    penjualan2 = models.penjualan2m.objects.all()
    total = 0
    for p in penjualan2:
      total += p.total()
    return render(req, 'penjualan/index4.html', {
        'data': penjualan2,
        'total': total,
    })

def penjualan_lain(req):
    penjualan3 = models.penjualan3m.objects.all()
    jumlah = 0
    jumlah2 = 0
    for j in penjualan3:
      jumlah += j.jumlah()
    
    for k in penjualan3:
      jumlah2 += k.jumlah2()
    return render(req, 'penjualan/index5.html', {
        'data': penjualan3,
        'jumlah': jumlah,
        'jumlah2': jumlah2,

    })

def piutang(req):
    penjualan2 = models.penjualan2m.objects.all()
    total = 0
    for p in penjualan2:
      total += p.total()
    return render(req, 'uangmasuk/index6.html', {
        'data': penjualan2,
        'total': total,
    })

def utang(req):
    utang = models.utangm.objects.all()
    return render(req, 'uangmasuk/index7.html', {
        'data': utang,
    })

def pend_lain(req):
    pend = models.pend_lainm.objects.all()
    return render(req, 'uangmasuk/index8.html', {
        'data': pend,
    })

def pembelian(req):
    return render(req, 'uangkeluar/index9.html')

def pembelian_tunai(req):
    pem = models.pem_tunaim.objects.all()
    return render(req, 'pembelian/index10.html', {
        'data': pem,
    })
    
def pembelian_kredit(req):
    pem = models.pem_kreditm.objects.all()
    return render(req, 'pembelian/index11.html', {
        'data': pem,
    })

def pembelian_lain(req):
    pem = models.pem_lainm.objects.all()
    return render(req, 'pembelian/index12.html', {
        'data': pem,
    })

def pembayaran_utang(req):
    return render(req, 'uangkeluar/index13.html')

def pembayaran_biaya(req):
    bayar = models.pembayaran_biayam.objects.all()
    return render(req, 'uangkeluar/index14.html', {
        'data': bayar,
    })

def pembayaran_lain(req):
    bayar = models.pembayaran_lainm.objects.all()
    return render(req, 'uangkeluar/index15.html', {
        'data': bayar,
    })

def barang(req):
    bayar = models.barangm.objects.all()
    return render(req, 'keperluan/index18.html', {
        'data': bayar,
    })





#crud
def penjualan1v(req):
    form_input = forms.penjualan1f()
    if req.POST:
        form_input = forms.penjualan1f(req.POST)
        if form_input.is_valid():
            form_input.save()
            return redirect('/penjualan_tunai')
    return render(req, 'crud/penjualan1.html', {
        'form': form_input,
    })

def penjualan2v(req):
    form_input = forms.penjualan2f()
    if req.POST:
        form_input = forms.penjualan2f(req.POST)
        if form_input.is_valid():
            form_input.save()
        return redirect('/penjualan_kredit')
    return render(req, 'crud/penjualan2.html', {
        'form': form_input,
    })

def penjualan3v(req):
    form_input = forms.penjualan3f()
    if req.POST:
        form_input = forms.penjualan3f(req.POST)
        if form_input.is_valid():
            form_input.save()
        return redirect('/penjualan_lain')
    return render(req, 'crud/penjualan3.html', {
        'form': form_input,
    })

def utangv(req):
    form_input = forms.utangf()
    if req.POST:
        form_input = forms.utangf(req.POST)
        if form_input.is_valid():
            form_input.save()
        return redirect('/utang')
    return render(req, 'crud/utang.html', {
        'form': form_input,
    })

def pend_lainv(req):
    form_input = forms.pend_lainf()
    if req.POST:
        form_input = forms.pend_lainf(req.POST)
        if form_input.is_valid():
            form_input.save()
        return redirect('/pend_lain')
    return render(req, 'crud/pend_lain.html', {
        'form': form_input,
    })

def pem_tunaiv(req):
    form_input = forms.pem_tunaif()
    if req.POST:
        form_input = forms.pem_tunaif(req.POST)
        if form_input.is_valid():
            form_input.save()
        return redirect('/pembelian_tunai')
    return render(req, 'crud/pem_tunai.html', {
        'form': form_input,
    })

def pem_kreditv(req):
    form_input = forms.pem_kreditf()
    if req.POST:
        form_input = forms.pem_kreditf(req.POST)
        if form_input.is_valid():
            form_input.save()
        return redirect('/pembelian_kredit')
    return render(req, 'crud/pem_kredit.html', {
        'form': form_input,
    })

def pem_lainv(req):
    form_input = forms.pem_lainf()
    if req.POST:
        form_input = forms.pem_lainf(req.POST)
        if form_input.is_valid():
            form_input.save()
        return redirect('/pembelian_lain')
    return render(req, 'crud/pem_lain.html', {
        'form': form_input,
    })

def pembayaran_biayav(req):
    form_input = forms.pembayaran_biayaf()
    if req.POST:
        form_input = forms.pembayaran_biayaf(req.POST)
        if form_input.is_valid():
            form_input.save()
        return redirect('/pembayaran_biaya')
    return render(req, 'crud/pembayaran_biaya.html', {
        'form': form_input,
    })

def pembayaran_lainv(req):
    form_input = forms.pembayaran_lainf()
    if req.POST:
        form_input = forms.pembayaran_lainf(req.POST)
        if form_input.is_valid():
            form_input.save()
        return redirect('/pembayaran_lain')
    return render(req, 'crud/pembayaran_lain.html', {
        'form': form_input,
    })

def barangv(req):
    form_input = forms.barangf()
    if req.POST:
        form_input = forms.barangf(req.POST)
        if form_input.is_valid():
            form_input.save()
        return redirect('/barang')
    return render(req, 'crud/barang.html', {
        'form': form_input,
    })










#edit
def edit_p_tunai(req, id):
    if req.POST:
        models.penjualan1m.objects.filter(pk=id).update(kuantitas=req.POST['kuantitas'], catatan=req.POST['catatan'])
        return redirect('/penjualan_tunai')

    penjualan = models.penjualan1m.objects.filter(pk=id).first()
    return render(req, 'penjualan/edit_p_tunai.html', {
        'data': penjualan,
    })

def edit_p_kredit(req, id):
    if req.POST:
        models.penjualan2m.objects.filter(pk=id).update(kuantitas=req.POST['kuantitas'], catatan=req.POST['catatan'])
        return redirect('/penjualan_kredit')

    penjualan = models.penjualan2m.objects.filter(pk=id).first()
    return render(req, 'penjualan/edit_p_kredit.html', {
        'data': penjualan,
    })

def edit_p_lain(req, id):
    if req.POST:
        models.penjualan3m.objects.filter(pk=id).update(keterangan=req.POST['keterangan'], kas=req.POST['kas'], piutang=req.POST['piutang'], catatan=req.POST['catatan'])
        return redirect('/penjualan_lain')

    penjualan = models.penjualan3m.objects.filter(pk=id).first()
    return render(req, 'penjualan/edit_p_lain.html', {
        'data': penjualan,
    })

def edit_utang(req, id):
    if req.POST:
        models.utangm.objects.filter(pk=id).update(keterangan=req.POST['keterangan'], jumlah=req.POST['jumlah'], catatan=req.POST['catatan'])
        return redirect('/utang')

    utang = models.utangm.objects.filter(pk=id).first()
    return render(req, 'uangmasuk/edit_utang.html', {
        'data': utang,
    })

def edit_pend_lain(req, id):
    if req.POST:
        models.pend_lainm.objects.filter(pk=id).update(keterangan=req.POST['keterangan'], jumlah=req.POST['jumlah'], catatan=req.POST['catatan'])
        return redirect('/pend_lain')

    pend = models.pend_lainm.objects.filter(pk=id).first()
    return render(req, 'uangmasuk/edit_pend_lain.html', {
        'data': pend,
    })

def edit_pem_tunai(req, id):
    if req.POST:
        models.pem_tunaim.objects.filter(pk=id).update(keterangan=req.POST['keterangan'], jumlah=req.POST['jumlah'], catatan=req.POST['catatan'])
        return redirect('/pembelian_tunai')

    pem = models.pem_tunaim.objects.filter(pk=id).first()
    return render(req, 'pembelian/edit_pem_tunai.html', {
        'data': pem,
    })

def edit_pem_kredit(req, id):
    if req.POST:
        models.pem_kreditm.objects.filter(pk=id).update(keterangan=req.POST['keterangan'], jumlah=req.POST['jumlah'], catatan=req.POST['catatan'])
        return redirect('/pembelian_kredit')

    pem = models.pem_kreditm.objects.filter(pk=id).first()
    return render(req, 'pembelian/edit_pem_kredit.html', {
        'data': pem,
    })

def edit_pem_lain(req, id):
    if req.POST:
        models.pem_lainm.objects.filter(pk=id).update(keterangan=req.POST['keterangan'], jumlah=req.POST['jumlah'], catatan=req.POST['catatan'])
        return redirect('/pembelian_lain')

    pem = models.pem_lainm.objects.filter(pk=id).first()
    return render(req, 'pembelian/edit_pem_lain.html', {
        'data': pem,
    })

def edit_pembayaran_biaya(req, id):
    if req.POST:
        models.pembayaran_biayam.objects.filter(pk=id).update(keterangan=req.POST['keterangan'], dibayar=req.POST['dibayar'], catatan=req.POST['catatan'])
        return redirect('/pembayaran_biaya')

    pem = models.pembayaran_biayam.objects.filter(pk=id).first()
    return render(req, 'uangkeluar/edit_pembayaran_biaya.html', {
        'data': pem,
    })

def edit_pembayaran_lain(req, id):
    if req.POST:
        models.pembayaran_lainm.objects.filter(pk=id).update(keterangan=req.POST['keterangan'], utang=req.POST['utang'], dibayar=req.POST['dibayar'], catatan=req.POST['catatan'])
        return redirect('/pembayaran_lain')

    pem = models.pembayaran_lainm.objects.filter(pk=id).first()
    return render(req, 'uangkeluar/edit_pembayaran_lain.html', {
        'data': pem,
    })

def edit_barang(req, id):
    if req.POST:
        models.barangm.objects.filter(pk=id).update(barang=req.POST['barang'], harga_beli=req.POST['harga_beli'], harga_jual=req.POST['harga_jual'])
        return redirect('/barang')

    pem = models.barangm.objects.filter(pk=id).first()
    return render(req, 'keperluan/edit_barang.html', {
        'data': pem,
    })

def edit_piutang(req, id):
    if req.POST:
        models.penjualan2m.objects.filter(pk=id).update(kuantitas=req.POST['kuantitas'], catatan=req.POST['catatan'])
        return redirect('/penjualan_kredit')

    penjualan = models.penjualan2m.objects.filter(pk=id).first()
    return render(req, 'penjualan/edit_p_kredit.html', {
        'data': penjualan,
    })







# Hapus
def hapus1(req, id):
    models.penjualan1m.objects.filter(pk=id).delete()
    return redirect('/penjualan_tunai')

def hapus2(req, id):
    models.penjualan2m.objects.filter(pk=id).delete()
    return redirect('/penjualan_kredit')

def hapus3(req, id):
    models.penjualan3m.objects.filter(pk=id).delete()
    return redirect('/penjualan_lain')