from django.shortcuts import render
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('input/', views.input),
    path('inputmovie/', views.inputmovie),
    path('<id>/', views.detail),
    path('<id>/delete/', views.delete),
    path('<id>/update/', views.update),
    path('<id>/movie', views.detailmovie),
    path('<id>/deletemovie/', views.deletemovie),
    path('<id>/updatemovie/', views.updatemovie),
]