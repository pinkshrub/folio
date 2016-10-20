from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def landing(request):
	print "landing"
	all_users = User.objects.all()
	context = {
		'users': all_users
	}
	return render(request, 'djlogreg/landing.html', context)

def login(request):
	if request.method == 'POST':
		print "step1"
		result = User.objects.login(request)
		print (result)
		if result[0] == False:
			messages.add_message(request, messages.INFO, 'your credentials did not match')
			return redirect('/')
		else:
			login_user(request, result[1])
			return redirect('/success')
	else:		
		return redirect('/')
	

def register(request):
	if request.method == "POST":
		result = User.objects.register(request)
		if result[0] == False:
			print "didnt work "
			for message in result[1]:
				print "here"
				messages.info(request, message)
			return redirect('/')
		else:
			print 'worked?'
			login_user(request, result[1])
			return redirect('/success')
			print 'registering'
	else:
		print "not a post bro"
		return redirect('/')
	

def success(request):
	print "successing"
	return render(request, 'djlogreg/success.html')

def login_user(request, user):
	request.session['curr_user'] = {
		'id'	: user.id,
		'first'	: user.first_name,
		'last'	: user.last_name,
		'email'	: user.email
	}

def logout(request):
	print "logging out?"
	request.session['curr_user'] = None
	return redirect('/')