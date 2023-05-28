from django.shortcuts import render,resolve_url,redirect
from django.http import HttpRequest

def home_page(request:HttpRequest):
    return render(request, "Guide/home.html")

def ula(request:HttpRequest):
    return render(request, "Guide/al-ula.html")
   
def dammam(request:HttpRequest):
    return render(request, "Guide/damam.html")

def jeddah(request:HttpRequest):
    
    return render(request, "Guide/jeddah.html")

def riyadh(request:HttpRequest):
    return render(request, "Guide/riyadh.html")


# Create your views here.
