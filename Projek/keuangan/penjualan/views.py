from django.shortcuts import render, redirect
from . import models, forms

# Create your views here.
def index(req):
	return render(req, 'penjualan_t/index.html')

def c_penjualan(req):
	
	penjualan = models.Penjualan.objects.all()
	return render(req, 'penjualan_t/penjualan.html',
		{
		'penjualan': penjualan,
		})


def i_penjualan(req):
  form_input = forms.PenjualanForm()

  if req.POST:
    form_input = forms.PenjualanForm(req.POST)

    if form_input.is_valid():
      form_input.save()

  penjualan = models.Penjualan.objects.all()
  return render(req, 'penjualan_t/penjualan_i.html', {
    'data': penjualan,
    'form': form_input,
  })

def r_penjualan(req, id):
	penjualan = models.Penjualan.objects.filter(pk=id).first()
	return render(req, 'penjualan_t/penjualan_r.html',
		{
		'penjualan': penjualan,
		})

def u_penjualan(req, id):
	if req.POST:
		models.Penjualan.objects.filter(pk=id).update(
		tanggal = req.POST['tgl'],
		keterangan = req.POST['ket'],
		jumlah = req.POST['jumlah'],
		catatan = req.POST['note'],
		)
		return redirect('/penjualan')

	penjualan = models.Penjualan.objects.filter(pk=id).first()

	return render(req, 'penjualan_t/penjualan_u.html',
		{
		'penjualan': penjualan,
		})

def d_penjualan(req, id):
	models.Penjualan.objects.filter(pk=id).delete()
	return redirect('/penjualan')