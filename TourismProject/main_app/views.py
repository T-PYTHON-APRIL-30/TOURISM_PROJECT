from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


def home_page(request: HttpRequest):


    return render(request, "main_app/home.html")

def taif_page(request: HttpRequest):


    return render(request, "main_app/taif.html")

def jeddah_page(request: HttpRequest):


    return render(request, "main_app/jeddah.html")

def riyadh_page(request: HttpRequest):


    return render(request, "main_app/riyadh.html")

def dark_mode(request:HttpRequest):
   
    response = redirect("main_app:home_page")
    response.set_cookie("mode", "dark")

    return response

def light_mode(request:HttpRequest):
    
    response = redirect("main_app:home_page")
    response.set_cookie("mode", "light")

    return response
