from django.shortcuts import render, redirect

from . import models, forms

def index(req):
  form_input = forms.PenjualanForm()

  if req.POST:
    form_input = forms.PenjualanForm(req.POST)

    if form_input.is_valid():
      form_input.save()
      return redirect(to='penjualan')

  tasks = models.Penjualan.objects.all()
  return render(req, 'penjualan/index.html', {
    'data': kass,
    'form': form_input,
  })

def detail(req, id):
  task = models.Penjualan.objects.filter(pk=id).first()
  return render(req, 'penjualan/detail.html', {
    'data': kas,
  })

def delete(req, id):
  models.Penjualan.objects.filter(pk=id).delete()
  return redirect('/')

def edit(req, id):
  if req.POST:
    task = models.Penjualan.objects.filter(pk=id).update(name=req.POST['name'])
    return redirect('/')

  task = models.Penjualan.objects.filter(pk=id).first()
  return render(req, 'penjualan/edit.html', {
    'data': kas,
  })