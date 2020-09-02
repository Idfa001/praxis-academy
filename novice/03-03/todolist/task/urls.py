from django.shortcuts import render
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('input/', views.input),
    path('<id>/', views.detail),
    path('<id>/delete/', views.delete),
    path('<id>/update/', views.update),
]