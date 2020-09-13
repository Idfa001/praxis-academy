from django.shortcuts import render
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.index, name='penjualan'),
    path('<id>/', views.detail),
    path('<id>/delete/', views.delete),
    path('<id>/edit', views.edit),
    
]