from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def homePage(request:HttpRequest):
    return render(request,'mainApp/index.html')

def aboutPage(request: HttpRequest):
    return render(request, 'mainApp/about.html')


def contactPage(request: HttpRequest):
    return render(request, 'mainApp/contact.html')

def galleryPage(request:HttpRequest):
    return render (request, 'mainApp/gallery.html')

def gallerySinglePage(request:HttpRequest):
    return render (request,'mainApp/gallery-single.html')

def riyadhPage(request:HttpRequest):
    return render (request,'mainApp/riyadh.html')

def makkahPage(request:HttpRequest):
    return render (request,'mainApp/makkah.html')

def alulaPage(request:HttpRequest):
    return render (request,'mainApp/alula.html')

def abhaPage(request:HttpRequest):
    return render (request,'mainApp/abha.html')