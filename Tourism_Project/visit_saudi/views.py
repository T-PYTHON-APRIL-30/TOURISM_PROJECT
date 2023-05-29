from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def home(request: HttpRequest):
    return render(request, "visit_saudi/home.html")


def riyadh(request: HttpRequest):
    return render(request, "visit_saudi/riyadh.html")


def abha(request: HttpRequest):
    return render(request, "visit_saudi/abha.html")


def mekkah(request: HttpRequest):
    return render(request, "visit_saudi/mekkah.html")


def alula(request: HttpRequest):
    return render(request, "visit_saudi/ula.html")
