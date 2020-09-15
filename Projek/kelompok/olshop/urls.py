"""kelompok URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.halamandepan),
    path('penjualan/', views.penjualan),
    path('penjualan_tunai/', views.penjualan_tunai),
    path('penjualan_kredit/', views.penjualan_kredit),
    path('penjualan_lain/', views.penjualan_lain),
    path('utang/', views.utang),
    path('piutang/', views.piutang),
    path('pend_lain/', views.pend_lain),
    path('pembelian/', views.pembelian),
    path('pembelian_tunai/', views.pembelian_tunai),
    path('pembelian_kredit/', views.pembelian_kredit),
    path('pembelian_lain/', views.pembelian_lain),
    path('pembayaran_utang/', views.pembayaran_utang),
    path('pembayaran_biaya/', views.pembayaran_biaya),
    path('pembayaran_lain/', views.pembayaran_lain),
    path('barang/', views.barang),
    path('admin/', admin.site.urls),


    #crud
    path('penjualan1/', views.penjualan1v),
    path('penjualan2/', views.penjualan2v),
    path('penjualan3/', views.penjualan3v),
    path('utangv/', views.utangv),
    path('pend_lainv/', views.pend_lainv),
    path('pem_tunaiv/', views.pem_tunaiv),
    path('pem_kreditv/', views.pem_kreditv),
    path('pem_lainv/', views.pem_lainv),
    path('pembayaran_biayav/', views.pembayaran_biayav),
    path('pembayaran_lainv/', views.pembayaran_lainv),
    path('barangv/', views.barangv),

    #edit
    path('<id>/edit_p_tunai/',views.edit_p_tunai),
    path('<id>/edit_p_kredit/',views.edit_p_kredit),
    path('<id>/edit_p_lain/',views.edit_p_lain),
    path('<id>/edit_utang/',views.edit_utang),
    path('<id>/edit_pend_lain/',views.edit_pend_lain),
    path('<id>/edit_pem_tunai/',views.edit_pem_tunai),
    path('<id>/edit_pem_kredit/',views.edit_pem_kredit),
    path('<id>/edit_pem_lain/',views.edit_pem_lain),
    path('<id>/edit_pembayaran_biaya/',views.edit_pembayaran_biaya),
    path('<id>/edit_pembayaran_lain/',views.edit_pembayaran_lain),
    path('<id>/edit_barang/',views.edit_barang),
]
