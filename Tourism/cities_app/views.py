from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def home_page(request:HttpRequest):
    return render(request,"cities_app/home_page.html")

def riyadh_page(request:HttpRequest):
    return render(request,"cities_app/riyadh_page.html")

def hail_page(request:HttpRequest):
    return render(request,"cities_app/hail_page.html")

def alula_page(request:HttpRequest):
    return render(request,"cities_app/alula_page.html")

def mekkah_page(request:HttpRequest):
    return render(request,"cities_app/mekkah_page.html")