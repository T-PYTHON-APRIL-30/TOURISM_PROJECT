from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def home_page(request:HttpRequest):
    return render (request, "welcome/home_page.html")

def Al_ahsa_page(request:HttpRequest):
    return render (request, "welcome/Al-ahsa_page.html")

def Al_ola_page(request:HttpRequest):
    return render (request, "welcome/Al-ola_page.html")

def Riyadh_page(request:HttpRequest):
    return render (request, "welcome/Riyadh_page.html")

def Jeedah_page(request:HttpRequest):
    return render (request, "welcome/jeedah_page.html")
