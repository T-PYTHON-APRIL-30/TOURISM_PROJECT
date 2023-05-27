from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.




def contact_page(request:HttpRequest):
    return render(request, "main_app/contact.html")

def home_page(request:HttpRequest):
    return render(request, "main_app/home.html")

def makkah_page(request:HttpRequest):
    return render(request, "main_app/makkah.html")

def riyadh_page(request:HttpRequest):
    return render(request, "main_app/riyadh.html")

def alula_page(request:HttpRequest):
    return render(request, "main_app/alula.html")

def jeddah_page(request:HttpRequest):
    return render(request, "main_app/jeddah.html")