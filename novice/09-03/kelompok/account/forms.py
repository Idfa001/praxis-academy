from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from . import models

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

		def clean(self):
			email = self.cleaned_data.get('email')
			if User.objects.filter(email=email).exists():
					raise ValidationError("Email exists")
			return self.cleaned_data