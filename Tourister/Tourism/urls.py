from django.urls import path
from . import views

app_name = "Tourism"

urlpatterns = [    
    path("test/", views.test_page, name="test_page"),
    path("", views.home_page, name="home_page"),
    path("city/alula", views.alula_page, name="alula_page"),
    path("city/mekkah", views.mekkah_page, name="mekkah_page"),
    path("city/dammam", views.dammam_page, name="dammam_page"),
    path("city/neom", views.neom_page, name="neom_page"),

]