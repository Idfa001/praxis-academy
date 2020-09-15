from django.shortcuts import render, redirect
from . import models, forms

# Create your views here.
def c_biaya(req):
	form_input = forms.BiayaForm()

	if req.POST:
		form_input = forms.BiayaForm(req.POST)
		if form_input.is_valid():
			form_input.save()

	biaya = models.Biaya.objects.all()

	return render(req, 'biaya_t/biaya.html',
		{
		'biaya': biaya,
		'form': form_input,
		})

def r_biaya(req, id):
	biaya = models.Biaya.objects.filter(pk=id).first()
	return render(req, 'biaya_t/biaya_r.html',
		{
		'biaya': biaya,
		})

def u_biaya(req, id):
	if req.POST:
		models.Biaya.objects.filter(pk=id).update(
		tanggal = req.POST['tgl'],
		keterangan = req.POST['ket'],
		bayar = req.POST['bayar'],
		hutang = req.POST['hutang'],
		catatan = req.POST['note'],
		)
		return redirect('/biaya')

	biaya = models.Biaya.objects.filter(pk=id).first()

	return render(req, 'biaya_t/biaya_u.html',
		{
		'biaya': biaya,
		})

def d_biaya(req, id):
	models.Biaya.objects.filter(pk=id).delete()
	return redirect('/biaya')