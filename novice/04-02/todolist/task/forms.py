from django.forms import ModelForm
from . import models

class TaskForm(ModelForm):
    class Meta:
        model = models.Task
        exclude = []

class MovieForm(ModelForm):
    class Meta:
        model = models.Movie
        exclude = []

class ComicForm(ModelForm):
    class Meta:
        model = models.Comic
        exclude = []