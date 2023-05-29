from django.shortcuts import render
from django.http import HttpRequest


# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def alula(request:HttpRequest):
    return render(request, 'app/alula.html')

def riyadh(request:HttpRequest):
    return render(request, 'app/riyadh.html')

def mecca(request:HttpRequest):
    return render(request, 'app/mecca.html')

def dhahran(request:HttpRequest):
    return render(request, 'app/dhahran.html')