from django.shortcuts import render
from django.http import HttpRequest
from .models import Videos
# Create your views here.

# def base(request):
#     videos =Videos.objects.all()
#     return render(request,"tourism/base.html", {'videos':videos})

def home_page(request:HttpRequest):
    videos =Videos.objects.all()

    return render(request,"tourism/home_page.html", {'videos':videos})

def riyadh(request:HttpRequest):
    videos =Videos.objects.all()
    return render(request,"tourism/riyadh.html", {'videos':videos})

def makkah(request:HttpRequest):
    videos =Videos.objects.all()
    return render(request,"tourism/makkah.html", {'videos':videos})

def Bisha(request:HttpRequest):
    videos =Videos.objects.all()
    return render(request,"tourism/bisha.html", {'videos':videos})

def Madinah(request:HttpRequest):
    videos =Videos.objects.all()
    return render(request,"tourism/madinah.html", {'videos':videos})

 