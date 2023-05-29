from django.shortcuts import render
from django.http import HttpRequest, HttpResponse 


# Create your views here.

def test_page(request: HttpRequest):
    return render(request, "Tourism/test_page.html")

def home_page(request: HttpRequest):
    return render(request, "Tourism/home_page.html")

def alula_page(request: HttpRequest):
    return render(request, "Tourism/alula_page.html")

def mekkah_page(request: HttpRequest):
    return render(request, "Tourism/mekkah_page.html")

def dammam_page(request: HttpRequest):
    return render(request, "Tourism/dammam_page.html")

def neom_page(request: HttpRequest):
    return render(request, "Tourism/neom_page.html")
