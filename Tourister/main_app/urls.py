from django.urls import path
from . import views

app_name= "main_app"

urlpatterns=[
    path('',views.home_page, name="home_page"),
    path('city/Riyadh/',views.riyadh_page,name="riyadh_page"),
    path('city/Abha/',views.abha_page,name="abha_page"),
    path('city/Makka/',views.makka_page,name="makka_page"),
    path('city/AlOla/',views.alola_page,name="alola_page"),
]