from django.shortcuts import render
from django.shortcuts import resolve_url

from django.http import HttpRequest,HttpResponse
# Create your views here.

def home_page(request:HttpRequest):

    return render(request,"main_app/home.html")

def riyadh_page(request:HttpRequest):
    return render(request, "main_app/riyadh.html")

def abha_page(request:HttpRequest):
    
    return render(request, "main_app/abha.html")

def makka_page(request:HttpRequest):
    
    return render(request, "main_app/makka.html")

def alola_page(request:HttpRequest):
    
    return render(request, "main_app/alola.html")