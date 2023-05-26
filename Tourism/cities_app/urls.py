from django.urls import path
from . import views

app_name = "cities_app"

urlpatterns = [ 
    path("", views.home_page, name="home_page"),
    path("city/riyadh/",views.riyadh_page,name="riyadh_page"),
    path("city/hail/",views.hail_page,name="hail_page"),
    path("city/mekkah/",views.mekkah_page,name="mekkah_page"),
    path("city/alula/",views.alula_page,name="alula_page"),
]