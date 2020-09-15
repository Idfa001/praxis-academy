from django.forms import ModelForm

from . import models

class PenjualanForm(ModelForm):
    class Meta:
        model = models.Penjualan
        exclude = []