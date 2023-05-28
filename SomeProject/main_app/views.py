from django.shortcuts import render, resolve_url, redirect
from django.http import HttpRequest, HttpResponse
from datetime import date
# Create your views here.


def home_page(request: HttpRequest):
    #to use template , we use render and pass in the path to the template
    return render(request, "main_app/base.html")


def dmmam(request:HttpRequest):

    return render(request, "main_app/dammam.html")


def riydah(request:HttpRequest):


    return render(request, "main_app/riydah.html")


def abha(request:HttpRequest):


    return render(request, "main_app/abha.html")

def makkah(request:HttpRequest):


    return render(request, "main_app/makkah.html")
