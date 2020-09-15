from django.forms import ModelForm

from . import models


class LainForm(ModelForm):
  class Meta:
    model = models.Lain
    exclude = [
      'done_at',
    ]
