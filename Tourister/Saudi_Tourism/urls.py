from django.urls import path
from . import views


name_app = "Saudi_Tourism"

urlpatterns = [
    path("", views.home_page, name= "home_page"),
    path("city/abha/", views.abha_page, name= "abha_page"),
    path("city/alula/", views.alula_page, name= "alula_page"),
    path("city/mekkah/", views.mekkah_page, name= "mekkah_page"),
    path("city/riyadh/", views.riyadh_page, name= "riyadh_page"),

]