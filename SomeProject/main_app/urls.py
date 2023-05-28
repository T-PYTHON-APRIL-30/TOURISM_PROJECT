from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("riyadh/", views.riydah, name="riydah"),
    path("dammam/", views.dmmam, name="dmmam"),
    path("makkah/", views.makkah, name="makkah"),
    path("abha/", views.abha, name="abha"),

]