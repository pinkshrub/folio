from django.contrib.auth.models import User
from django.forms import ModelForm

class userRegForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']

class userLogForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']