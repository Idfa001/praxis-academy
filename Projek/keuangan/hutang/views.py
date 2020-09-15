from django.shortcuts import render, redirect
from . import models, forms

# Create your views here.
def c_hutang(req):
	form_input = forms.HutangForm()

	if req.POST:
		form_input = forms.HutangForm(req.POST)
		if form_input.is_valid():
			form_input.save()

	hutang = models.Hutang.objects.all()

	return render(req, 'hutang_t/hutang.html',
		{
		'hutang': hutang,
		'form': form_input,
		})

def r_hutang(req, id):
	hutang = models.Hutang.objects.filter(pk=id).first()
	return render(req, 'hutang_t/hutang_r.html',
		{
		'hutang': hutang,
		})

def u_hutang(req, id):
	if req.POST:
		models.Hutang.objects.filter(pk=id).update(
		tanggal = req.POST['tgl'],
		keterangan = req.POST['ket'],
		jumlah = req.POST['jumlah'],
		catatan = req.POST['note'],
		)
		return redirect('/hutang')

	hutang = models.Hutang.objects.filter(pk=id).first()

	return render(req, 'hutang_t/hutang_u.html',
		{
		'hutang': hutang,
		})

def d_hutang(req, id):
	models.Hutang.objects.filter(pk=id).delete()
	return redirect('/hutang')