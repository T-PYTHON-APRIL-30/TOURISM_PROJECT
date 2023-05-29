from django.shortcuts import render, resolve_url
from django.http import HttpRequest, HttpResponse


# Create your views here.

def home_page(request:HttpRequest):

    return render(request, "Saudi_Tourism/home_page.html")

def abha_page(request:HttpRequest):

    
    return render(request, "Saudi_Tourism/abha.html")

def alula_page(request:HttpRequest):

    return render(request, "Saudi_Tourism/alula.html")

def mekkah_page(request:HttpRequest):

    return render(request, "Saudi_Tourism/mekkah.html")

def riyadh_page(request:HttpRequest):

    return render(request, "Saudi_Tourism/riyadh.html")