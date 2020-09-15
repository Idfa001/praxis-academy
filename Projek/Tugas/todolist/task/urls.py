from django.shortcuts import render
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('buying', views.buying, name='buying'),
    path('selling', views.selling, name='selling'),
    path('customer', views.customer, name='customer'),
    path('customerdetail/<id>/', views.customerdetail),
    path('customeredit/<id>/', views.customeredit),
    path('customerdelete/<id>/', views.customerdelete),
    path('supplier', views.supplier, name='supplier'),
    path('supplierdetail/<id>/', views.supplierdetail),
    path('supplieredit/<id>/', views.supplieredit),
    path('supplierdelete/<id>/', views.supplierdelete),
    path('item/', views.item, name='item'),
    path('itemdetail/<id>/', views.itemdetail),
    path('itemedit/<id>/', views.itemedit),
    path('itemdelete/<id>/', views.itemdelete),
    #path('/<id>/', views.customerdetail),
    
    #path('<id>/delete/', views.supplierdelete),
    #path('<id>/', views.detail),
    #path('<id>/delete/', views.delete),
    #path('<id>/edit/', views.edit),
]
