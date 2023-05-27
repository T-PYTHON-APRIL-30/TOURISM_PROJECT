from django.urls import path
from . import views

app_name="tourism"

urlpatterns=[
    path("", views.home_page,name="home_page"),
    path("riyadh",views.riyadh,name="riyadh_page"),
    path("makkah", views.makkah,name="makkah_page"),
    path("bisha", views.Bisha,name="bisha_page"),
    path("madinah",views.Madinah,name="madinah_page")

]