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
    penjualan3 = models.penjualan3m.objects.all()
    pend = models.pend_lainm.objects.all()


    total_saldo = 0
    total_terima = 0   
 
    for p in penjualan2:
      total_saldo += p.saldo()
      total_terima += p.terima

    total_saldo1 = 0
    total_terima1 = 0

    for p in penjualan3:
      total_saldo1 += p.saldo()
      total_terima1 += p.terima

    total_saldo2 = 0
    total_terima2 = 0   
 
    for p in pend:
      total_saldo2 += p.saldo()
      total_terima2 += p.terima

    saldo_total1 = total_saldo + total_saldo1 + total_saldo2
    saldo_total2 = total_terima + total_terima1 + total_terima2
    return render(req, 'uangmasuk/index6.html', {
        'data': penjualan2,
        'data1': penjualan3,
        'data2': pend,
        'saldo_total1': saldo_total1,
        'saldo_total2': saldo_total2,
        
    })

def utang(req):
    utang = models.utangm.objects.all()
    jum_utang = 0
    for i in utang:
      jum_utang += i.jum_utang()

    return render(req, 'uangmasuk/index7.html', {
        'data': utang,
        'jum_utang': jum_utang,
        
    })

def pend_lain(req):
    pend = models.pend_lainm.objects.all()
    jum_pend = 0
    jum_pend1 = 0
    for i in pend:
      jum_pend += i.jum_pend()
      jum_pend1 += i.jum_pend1()
    return render(req, 'uangmasuk/index8.html', {
        'data': pend,
        'jum_pend': jum_pend,
        'jum_pend1': jum_pend1,
    })

def pembelian(req):
    return render(req, 'uangkeluar/index9.html')

def pembelian_tunai(req):
    pem = models.pem_tunaim.objects.all()
    jum_pem = 0
    for i in pem:
      jum_pem += i.jum_pem()
    return render(req, 'pembelian/index10.html', {
        'data': pem,
        'jum_pem': jum_pem,
    })
    
def pembelian_kredit(req):
    pem = models.pem_kreditm.objects.all()
    jum_pem = 0
    for i in pem:
      jum_pem += i.jum_pem()
    return render(req, 'pembelian/index11.html', {
        'data': pem,
        'jum_pem': jum_pem,
    })

def pembelian_lain(req):
    pem = models.pem_lainm.objects.all()
    jum_pem = 0
    jum_pem1 = 0
    for i in pem:
      jum_pem += i.jum_pem()
      jum_pem1 += i.jum_pem1()
    return render(req, 'pembelian/index12.html', {
        'data': pem,
        'jum_pem': jum_pem,
        'jum_pem1': jum_pem1,
    })


def pembayaran_utang(req):
    utang = models.utangm.objects.all()
    pem = models.pem_kreditm.objects.all()
    pem1 = models.pem_lainm.objects.all()
    bayar = models.pembayaran_lainm.objects.all()

    jum_utang = 0
    total_saldo = 0
    total_dibayar = 0

    for i in utang:
      jum_utang += i.jum_utang()

    for u in utang:
        total_saldo += u.saldo()
        total_dibayar += u.dibayar

    total_saldo1 = 0
    total_dibayar1 = 0

    for u in pem:
        total_saldo1 += u.saldo()
        total_dibayar1 += u.dibayar1

    total_saldo2 = 0
    total_dibayar2 = 0

    for u in pem1:
        total_saldo2 += u.saldo()
        total_dibayar2 += u.dibayar2

    total_saldo3 = 0
    total_dibayar3 = 0

    for u in bayar:
        total_saldo3 += u.saldo()
        total_dibayar3 += u.dibayar3

    jumlah1 = total_saldo + total_saldo1 + total_saldo2 + total_saldo3
    jumlah2 = total_dibayar + total_dibayar1 + total_dibayar2 + total_dibayar3

    return render(req, 'uangkeluar/index13.html', {
        'data': utang,
        'data1': pem,
        'data2': pem1,
        'data3': bayar,
        'jum_utang': jum_utang,
        'jumlah1': jumlah1,
        'jumlah2': jumlah2,
    })

def pembayaran_biaya(req):
    bayar = models.pembayaran_biayam.objects.all()
    jum_pem = 0
    for i in bayar:
      jum_pem += i.jum_pem()

    return render(req, 'uangkeluar/index14.html', {
        'data': bayar,
        'jum_pem': jum_pem,
    })

def pembayaran_lain(req):
    bayar = models.pembayaran_lainm.objects.all()
    jum1 = 0
    jum2 = 0
    for i in bayar:
        jum1 += i.jum1()
        jum2 += i.jum2()
    return render(req, 'uangkeluar/index15.html', {
        'data': bayar,
        'jum1': jum1,
        'jum2': jum2,
    })

def barang(req):
    bayar = models.barangm.objects.all()
    return render(req, 'keperluan/index18.html', {
        'data': bayar,
    })

def lr(req):

# saldo awal

# uang masuk
    penjualan1 = models.penjualan1m.objects.all()
    total1 = 0
    for p in penjualan1:
        total1 += p.total()

    penjualan3 = models.penjualan3m.objects.all()
    total2 = 0
    for p in penjualan3:
      total2 += p.jumlah()

    penjualan2 = models.penjualan2m.objects.all()
    penjualan3 = models.penjualan3m.objects.all()
    pend = models.pend_lainm.objects.all()

    total_terima = 0   
 
    for p in penjualan2:
      total_terima += p.terima

    total_terima1 = 0

    for p in penjualan3:
      total_terima1 += p.terima

    total_terima2 = 0   
 
    for p in pend:
      total_terima2 += p.terima

    total3 = total_terima + total_terima1 + total_terima2

    utang = models.utangm.objects.all()
    total4 = 0
    for p in utang:
        total4 += p.jum_utang()

    pend = models.pend_lainm.objects.all()
    total5 = 0
    for p in pend:
      total5 += p.jum_pend()

# uang keluar
    pem = models.pem_tunaim.objects.all()
    total6 = 0
    for p in pem:
      total6 += p.jum_pem()

    pem1 = models.pem_lainm.objects.all()
    total7 = 0
    for p in pem1:
      total7 += p.jum_pem()

    # total8 pembayaran utang
    utang = models.utangm.objects.all()
    pem = models.pem_kreditm.objects.all()
    pem1 = models.pem_lainm.objects.all()

    total_dibayar = 0


    for u in utang:
        total_dibayar += u.dibayar

    total_dibayar1 = 0

    for u in pem:
        total_dibayar1 += u.dibayar1

    total_dibayar2 = 0

    for u in pem1:
        total_dibayar2 += u.dibayar2

    total8 = total_dibayar + total_dibayar1 + total_dibayar2

    bayar = models.pembayaran_biayam.objects.all()
    total9 = 0
    for p in bayar:
      total9 += p.jum_pem()

    bayar2 = models.pembayaran_lainm.objects.all()
    total10 = 0
    for p in bayar2:
        total10 += p.jum1()

    sawal = models.penjualan1m.objects.all()
    saldo1 = 0
    for p in sawal:
        saldo1 += p.saldo_awal

    total_semua1 = total1 + total2 + total3 + total4 + total5
    total_semua2 = total6 + total7 + total8 + total9 + total10
    laba_rugi = total_semua1 - total_semua2
    akhir = saldo1 + laba_rugi
    print(sawal)

    return render(req, 'keperluan/index16.html', {
        'penjualan1': penjualan1.first(),
        'total1': total1,
        'total2': total2,
        'total3': total3,   #koreksi
        'total4': total4,
        'total5': total5,
        'total6': total6,
        'total7': total7,
        'total8': total8,
        'total9': total9,
        'total10': total10,
        'total_semua1': total_semua1,
        'total_semua2': total_semua2,
        'laba_rugi': laba_rugi,
        'saldo': saldo1,
        'akhir': akhir,
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

def edit_p_kredit_terima(req, id):
    if req.POST:
        models.penjualan2m.objects.filter(pk=id).update(terima=req.POST['terima'])
        return redirect('/piutang')

    penjualan = models.penjualan2m.objects.filter(pk=id).first()
    return render(req, 'uangmasuk/edit_piutang.html', {
        'data': penjualan,
    })

def edit_p_kredit_terima1(req, id):
    if req.POST:
        models.penjualan3m.objects.filter(pk=id).update(terima=req.POST['terima'])
        return redirect('/piutang')

    penjualan = models.penjualan3m.objects.filter(pk=id).first()
    return render(req, 'uangmasuk/edit_piutang1.html', {
        'data1': penjualan,
    })

def edit_pend_lain_terima(req, id):
    if req.POST:
        models.pend_lainm.objects.filter(pk=id).update(terima=req.POST['terima'])
        return redirect('/piutang')

    penjualan = models.pend_lainm.objects.filter(pk=id).first()
    return render(req, 'uangmasuk/edit_terimalain.html', {
        'data2': penjualan,
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
        models.pend_lainm.objects.filter(pk=id).update(keterangan=req.POST['keterangan'], jumlah=req.POST['jumlah'], piutang=req.POST['piutang'], catatan=req.POST['catatan'])
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
        models.pem_lainm.objects.filter(pk=id).update(keterangan=req.POST['keterangan'], dibayar=req.POST['dibayar'], utang=req.POST['utang'], catatan=req.POST['catatan'])
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

def edit_butang(req, id):
    if req.POST:
        models.utangm.objects.filter(pk=id).update(dibayar=req.POST['dibayar'])
        return redirect('/pembayaran_utang')

    utang = models.utangm.objects.filter(pk=id).first()
    return render(req, 'uangkeluar/edit_butang.html', {
        'data': utang,
    })

def edit_butang1(req, id):
    if req.POST:
        models.pem_kreditm.objects.filter(pk=id).update(dibayar1=req.POST['dibayar1'])
        return redirect('/pembayaran_utang')

    utang = models.pem_kreditm.objects.filter(pk=id).first()
    return render(req, 'uangkeluar/edit_butang1.html', {
        'data': utang,
    })

def edit_butang2(req, id):
    if req.POST:
        models.pem_lainm.objects.filter(pk=id).update(dibayar2=req.POST['dibayar2'])
        return redirect('/pembayaran_utang')

    utang = models.pem_lainm.objects.filter(pk=id).first()
    return render(req, 'uangkeluar/edit_butang2.html', {
        'data': utang,
    })

def edit_butang3(req, id):
    if req.POST:
        models.pembayaran_lainm.objects.filter(pk=id).update(dibayar3=req.POST['dibayar3'])
        return redirect('/pembayaran_utang')

    utang = models.pembayaran_lainm.objects.filter(pk=id).first()
    return render(req, 'uangkeluar/edit_butang3.html', {
        'data': utang,
    })

def edit_saldoawal(req, id):
    if req.POST:
        models.penjualan1m.objects.filter(pk=id).update(saldo_awal=req.POST['saldo_awal'])
        return redirect('/lr')

    penjualan = models.penjualan1m.objects.filter(pk=id).first()
    return render(req, 'keperluan/edit_saldo.html', {
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

def hapus4(req, id):
    models.utangm.objects.filter(pk=id).delete()
    return redirect('/utang')

def hapus5(req, id):
    models.pem_tunaim.objects.filter(pk=id).delete()
    return redirect('/pembelian_tunai')

def hapus6(req, id):
    models.pem_kreditm.objects.filter(pk=id).delete()
    return redirect('/pembelian_kredit')

def hapus7(req, id):
    models.pem_lainm.objects.filter(pk=id).delete()
    return redirect('/pembelian_lain')

def hapus8(req, id):
    models.pembayaran_biayam.objects.filter(pk=id).delete()
    return redirect('/pembayaran_biaya')

def hapus9(req, id):
    models.pembayaran_lainm.objects.filter(pk=id).delete()
    return redirect('/pembayaran_lain')