from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.

def home_page(request:HttpRequest):

    return render(request, "main_app/home.html")

def riyadh(request:HttpRequest):

    return render(request, "main_app/riyadh.html")

def abha(request:HttpRequest):

    return render(request, "main_app/abha.html")

def mekkah(request:HttpRequest):

    return render(request, "main_app/mekkah.html")

def almadinah(request:HttpRequest):

    return render(request, "main_app/almadinah.html")