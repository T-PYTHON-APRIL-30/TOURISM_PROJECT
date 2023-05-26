from django.urls import path
from . import views


app_name = 'main_app'

urlpatterns = [
    path('', views.home_page, name = 'home_page'),
    path('city/', views.city_page, name = 'city_page'),
    path('city/Riyadh/', views.riyadh_city, name = 'riyadh_city'),
    path('city/Abha/', views.abha_city, name = 'abha_city'),
    path('city/Mekkah/', views.mekkah_city, name = 'mekkah_city'),
    path('city/AlUla/', views.alula_city, name = 'alula_city')
]
