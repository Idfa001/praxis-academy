
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('kas.urls')),
    path('lain/', include('lain.urls')),
    
]
