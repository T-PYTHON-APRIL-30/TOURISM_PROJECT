from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def home(request:HttpRequest):

    return HttpResponse('Home')

def riyadh(request:HttpRequest):

    return HttpResponse('riyadh')

def abha(request:HttpRequest):

    return HttpResponse('abha')

def mekkah(request:HttpRequest):

    return HttpResponse('mekkah')

def alula(request:HttpRequest):

    return HttpResponse('AlUla')





