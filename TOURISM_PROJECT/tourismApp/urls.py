from django.contrib import admin
from django.urls import path,include
from . import views
app_name = "tourismApp"
urlpatterns = [
    path('', views.home, name='home'),
    path('Riyadh/',views.RiyadhPage,name='Riyadh'),
    path('Abha/',views.AbhaPage,name='Abha'),
    path('Alola/',views.AlolaPage,name='Alola'),
]