from django.urls import path
from . import views
from .models import Videos

app_name="tourism"

urlpatterns=[
    path("", views.home_page,name="home_page"),
    path("city/riyadh",views.riyadh,name="riyadh_page"),
    path("city/makkah", views.makkah,name="makkah_page"),
    path("city/bisha", views.Bisha,name="bisha_page"),
    path("city/madinah",views.Madinah,name="madinah_page")

]