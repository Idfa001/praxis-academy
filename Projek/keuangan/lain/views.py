from django.shortcuts import render, redirect

from . import models, forms

def index (req):

    lain = models.Lain.objects.all()
    return render(req, 'lain/lain.html', {
        'data': lain,
    })


def lain (req):

    lain = models.Lain.objects.all()
    return render(req, 'lain/lain.html', {
        'data': lain,
    })

def input(req):
  form_input = forms.LainForm()

  if req.POST:
    form_input = forms.LainForm(req.POST)

    if form_input.is_valid():
      form_input.save()

  lain = models.Lain.objects.all()
  return render(req, 'lain/input.html', {
    'data': lain,
    'form': form_input,
  })

def delete(req, id):
  models.Lain.objects.filter(pk=id).delete()
  return redirect('/')

def edit(req, id):
  if req.POST:
    lain = models.Lain.objects.filter(pk=id).update(keterangan=req.POST['keterangan'], kas=req.POST['kas'], piutang=req.POST['piutang'], catatan=req.POST['catatan'])
    return redirect('/')

  lain = models.Lain.objects.filter(pk=id).first()
  return render(req, 'lain/edit.html', {
    'data': lain,
  })

