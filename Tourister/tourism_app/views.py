from django.shortcuts import render

def home(request):
    return render(request, 'tourism_app/home.html')

def city(request):
    return render(request, 'tourism_app/city.html')

def riyadh(request):
    return render(request, 'tourism_app/riyadh.html')

def abha(request):
    return render(request, 'tourism_app/abha.html')

def makkah(request):
    return render(request, 'tourism_app/makkah.html')

def alula(request):
    return render(request, 'tourism_app/alula.html')
