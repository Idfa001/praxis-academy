from django.forms import ModelForm

from . import models

class HutangForm(ModelForm):
    class Meta:
        model = models.Hutang
        exclude = []