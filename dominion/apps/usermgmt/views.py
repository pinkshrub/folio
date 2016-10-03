from django.shortcuts import render
from .forms import Regform, Logform

# Create your views here.
def Landing(request):
	context = {
		'regform': Regform,
		'logform': Logform
	}
	return render(request, "usermgmt/landing.html")