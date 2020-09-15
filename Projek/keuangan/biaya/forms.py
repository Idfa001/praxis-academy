from django.forms import ModelForm

from . import models

class BiayaForm(ModelForm):
    class Meta:
        model = models.Biaya
        exclude = []