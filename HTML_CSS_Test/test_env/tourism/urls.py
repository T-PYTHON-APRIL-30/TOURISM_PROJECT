from django.urls import path
from . import views

app_name = "tourism"

urlpatterns = [
    path('home/',views.home_page, name="home_page"),
    path('about/saudi/',views.about_sa, name="about_sa"),
    path('riyadh/',views.riyadh_page, name="riyadh_page"),
    path('alula/',views.alula_page, name="alula_page"),
    path('jeddah/',views.jeddah_page, name="jeddah_page"),
    path('abha/',views.abha_page, name="abha_page"),
]