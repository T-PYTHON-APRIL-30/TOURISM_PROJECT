from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("city/taif/", views.taif_page, name="taif_page"),
    path("city/riyadh/", views.riyadh_page, name="riyadh_page"),
    path("city/jeddah/", views.jeddah_page, name="jeddah_page"),
    path("mode/dark/", views.dark_mode, name="dark_mode"),
    path("mode/light/", views.light_mode, name="light_mode")

]