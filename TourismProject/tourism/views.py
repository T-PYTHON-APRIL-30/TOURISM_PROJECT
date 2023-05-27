from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.

def home_page(request:HttpRequest):
    
    return render(request,"tourism/home_page.html")

def riyadh(request:HttpRequest):

    return render(request,"tourism/riyadh.html")

def makkah(request:HttpRequest):

    return render(request,"tourism/makkah.html")

def Bisha(request:HttpRequest):

    return render(request,"tourism/bisha.html")

def Madinah(request:HttpRequest):

    return render(request,"tourism/madinah.html")
