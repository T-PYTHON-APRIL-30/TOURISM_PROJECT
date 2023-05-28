from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("city/Riyadh/", views.riyadh_page, name="riyadh_page"),
    path("city/Dammam/", views.dammam_page, name="dammam_page"),
    path("city/Jeddah/", views.jeddah_page, name="jeddah_page"),
    path("city/AlUla/", views.alUla_page, name="alUla_page")
]