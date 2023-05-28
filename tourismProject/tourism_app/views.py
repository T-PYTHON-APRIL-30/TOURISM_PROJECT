from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.shortcuts import resolve_url
# Create your views here.
def home_page(request:HttpRequest):
    resolve_url("tourism_app:home_page")
    resolve_url("tourism_app:abha_page")
    resolve_url("tourism_app:riyadh_page")
    resolve_url("tourism_app:jeddah_page")
    resolve_url("tourism_app:AlUla_page")
    return render(request,"tourism_app/home.html")

def abha_page(request:HttpRequest):
   
    return render(request,"tourism_app/abha.html")

def riyadh_page(request:HttpRequest):
   
    return render(request,"tourism_app/riyadh.html")

def jeddah_page(request:HttpRequest):
   
    return render(request,"tourism_app/jeddah.html")

def AlUla_page(request:HttpRequest):
   
    return render(request,"tourism_app/AlUla.html")



