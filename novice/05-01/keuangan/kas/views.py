from django.shortcuts import render, redirect

from . import models, forms

def index (req):

    kas = models.Penjualan.objects.all()
    return render(req, 'kas/index.html', {
        'data': kas,
    })

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
      return redirect(to='penjualan')

  kas = models.Penjualan.objects.all()
  return render(req, 'penjualan/input.html', {
    'data': kas,
    'form': form_input,
  })

def detail(req, id):
  kas = models.Penjualan.objects.filter(pk=id).first()
  return render(req, 'penjualan/detail.html', {
    'data': keuangan,
  })

def delete(req, id):
  models.Penjualan.objects.filter(pk=id).delete()
  return redirect('/')

def edit(req, id):
  if req.POST:
    kas = models.Penjualan.objects.filter(pk=id).update(name=req.POST['name'])
    return redirect('/')

  kas = models.Penjualan.objects.filter(pk=id).first()
  return render(req, 'penjualan/edit.html', {
    'data': kas,
  })