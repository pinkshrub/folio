from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def landing(request):
	return render(request, 'djlogreg/landing.html')

def login(request):
	if request.method is not 'POST':
		return redirect('/')
	result = User.objects.login(request)
	if result[0] == False:
		messages.add_message(request, messages.INFO, 'your credentials did not match')
		return redirect('/')
	else:
		session['curr_user']=result[1]
		return redirect('/success')

def register(request):
	if request.method is not 'POST':
		print "not a post bro"
		return redirect('/')
	result = User.objects.register(request)
	if result[0] == False:
		print "didnt work "
		for message in result[1]:
			messages.add_message(request, messages.INFO, message)
		return redirect('/')
	else:
		print 'worked?'
		session['curr_user'] = result[1]
		return redirect('/success')

def success(request):
	return render(request, 'djlogreg/success.html')