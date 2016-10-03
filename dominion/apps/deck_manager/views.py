from django.shortcuts import render, redirect
from .forms import userRegForm, userLogForm
from django.contrib.auth import authenticate, login
from .models import Card, Kingdom, Kingdoms_Cards, Game, Rating
from django.contrib.auth.models import User
import bcrypt

# Create your views here.
def landing(request):
	context = {
		'user_reg_form' : userRegForm,
		'user_log_form'	: userLogForm,
	}
	return render(request, 'deck_manager/landing.html', context)

# WORKING HERE
def register(request):
	new_user = userRegForm(request.POST)
	if new_user.is_valid():
		user = new_user.save(commit=False)
		user.save
		login_user = authenticate(username=user.username, password=user.password)
		if login_user is not None:
			return render(request, 'deck_manager/main.html')
		else:
			return redirect('/')
	else:
		pass



def log_in(request):
	pass

def main(request):
	return render(request, 'deck_manager/main.html', context)
