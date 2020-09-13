
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('keuangan.urls')),
    path('admin/', admin.site.urls),
]