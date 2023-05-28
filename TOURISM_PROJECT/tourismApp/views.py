from django.shortcuts import render
from django.http import HttpRequest,HttpResponse


def home (request:HttpRequest):
    variable1='hello'
    context={'key1':variable1}
    return render(request,"tourismApp/home.html",context)

def RiyadhPage (request:HttpRequest):
    variable2='welcome in Riyadh'
    context={'key2':variable2}
    return render(request,"tourismApp/Riyadh.html",context)

def AbhaPage (request:HttpRequest):
    variable3='welcome in Abha'
    context={'key3':variable3}
    return render(request,"tourismApp/Abha.html",context)

def AlolaPage (request:HttpRequest):
    variable4='welcome in Alola'
    context={'key4':variable4}
    return render(request,"tourismApp/Alola.html",context)

# Create your views here.
