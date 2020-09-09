from django.shortcuts import render
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.index),
    path('about/', views.about),
    path('music/', views.music),
    path('movie/', views.movie),
    path('comic/', views.comic),

    path('input/', views.input),
    path('inputmovie/', views.inputmovie),
    path('inputcomic/', views.inputcomic),
    
    path('<id>/', views.detail),
    path('<id>/delete/', views.delete),
    path('<id>/update/', views.update),
    
    path('<id>/movie', views.detailmovie),
    path('<id>/deletemovie/', views.deletemovie),
    path('<id>/updatemovie/', views.updatemovie),

    path('<id>/comic', views.detailcomic),
    path('<id>/deletecomic/', views.deletecomic),
    path('<id>/updatecomic/', views.updatecomic),
    
]
