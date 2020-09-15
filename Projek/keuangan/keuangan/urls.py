
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('kas.urls')),
    path('lain/', include('lain.urls')),

    path('penjualan/', include('penjualan.urls')),
    path('biaya/', include('biaya.urls')),
    path('hutang/', include('hutang.urls')),

    path('admin/', admin.site.urls),
    
]
