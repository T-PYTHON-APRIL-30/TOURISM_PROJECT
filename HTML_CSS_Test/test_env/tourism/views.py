from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def home_page(request):

    return render(request,"tourism/home.html")

def about_sa(request):

    return render(request,"tourism/about_sa.html")

def riyadh_page(request):

    return render(request,"tourism/riyadh.html")

def alula_page(request):

    return render(request,"tourism/alula.html")

def jeddah_page(request):

    return render(request,"tourism/jeddah.html")

def abha_page(request):

    return render(request,"tourism/abha.html")