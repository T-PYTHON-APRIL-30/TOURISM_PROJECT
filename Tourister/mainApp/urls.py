from . import views
from django.urls import path

app_name = 'mainApp'

urlpatterns = [
    path('',views.homePage, name='homePage'),
    path('about',views.aboutPage, name='aboutPage'),
    path('contact',views.contactPage, name='contactPage'),
    path('gallery/', views.galleryPage, name='galleryPage'),
    path('gallery/city-gallery', views.gallerySinglePage, name='gallerySinglePage'),
    path('city/Riyadh/', views.riyadhPage, name='riyadhPage'),
    path('city/Makkah/', views.makkahPage, name='makkahPage'),
    path('city/AlUla/', views.alulaPage, name='alulaPage'),
    path('city/Abha/', views.abhaPage, name='abhaPage')
    
    
]

