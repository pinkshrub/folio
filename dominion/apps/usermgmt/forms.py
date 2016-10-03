from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contriblauth.forms import UserCreationForm


class Regform(UserCreationForm):
	email=forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['username', 'email','password1','password2']

	def save(self, commit=True):
		user=super(RegForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		if commit:
			user.save()
		return user

class Logform(ModelForm):
	class Meta:
		model = User
		fields = ['email', 'password']
