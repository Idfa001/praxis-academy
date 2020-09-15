from django.shortcuts import render, redirect

from . import models, forms

def index (req):

    kas = models.Penjualan.objects.all()
    return render(req, 'kas/index.html', {
        'data': kas,
    })

def index2 (req):
    return render(req, 'kas/index2.html')

def index3 (req):
    return render(req, 'kas/index3.html')

def about (req):

    kas = models.Penjualan.objects.all()
    return render(req, 'kas/about.html', {
        'data': kas,
    })

def penjualan (req):

    kas = models.Penjualan.objects.all()
    return render(req, 'kas/penjualan/penjualan.html', {
        'data': kas,
    })

def input(req):
  form_input = forms.PenjualanForm()

  if req.POST:
    form_input = forms.PenjualanForm(req.POST)

    if form_input.is_valid():
      form_input.save()

  kas = models.Penjualan.objects.all()
  return render(req, 'kas/penjualan/input.html', {
    'data': kas,
    'form': form_input,
  })

def delete(req, id):
  models.Penjualan.objects.filter(pk=id).delete()
  return redirect('/')

def edit(req, id):
  if req.POST:
    kas = models.Penjualan.objects.filter(pk=id).update(nama_barang=req.POST['nama_barang'], jumlah_barang=req.POST['jumlah_barang'])
    return redirect('/')

  kas = models.Penjualan.objects.filter(pk=id).first()
  return render(req, 'kas/penjualan/edit.html', {
    'data': kas,
  })

