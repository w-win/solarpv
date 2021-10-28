from django.shortcuts import render


# Create your views here.

def index(request):
	return render(request, 'solarpvapp/Homepage.html')


def Menu1(request):
	return render(request, 'solarpvapp/Menu1.html')


def Register(request):
	return render(request, 'solarpvapp/registeration.html')


