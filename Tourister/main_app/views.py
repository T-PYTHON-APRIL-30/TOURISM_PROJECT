from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def home_page(request: HttpRequest):
    return render(request, 'main_app/home.html')


def city_page(request: HttpRequest):
    return render(request, 'main_app/city.html')


def riyadh_city(request: HttpRequest):
    return render(request, 'main_app/riyadh.html')


def abha_city(request: HttpRequest):
    return render(request, 'main_app/abha.html')


def mekkah_city(request: HttpRequest):
    return render(request, 'main_app/mekkah.html')


def alula_city(request: HttpRequest):
    return render(request, 'main_app/alula.html')
