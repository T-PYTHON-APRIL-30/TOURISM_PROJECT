from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
# Create your views here.


def home_page(request: HttpRequest):
    #to use template , we use render and pass in the path to the template
    return render(request, "main_app/home.html")


def riyadh_page(request:HttpRequest):
    return render(request, "main_app/riyadh.html")

def dammam_page(request:HttpRequest):
    return render(request, "main_app/dammam.html")

def jeddah_page(request:HttpRequest):
    return render(request, "main_app/jeddah.html")

def alUla_page(request:HttpRequest):
    return render(request, "main_app/alUla.html")