from django.urls import path
from . import views

app_name="tourism_app"
urlpatterns = [
    path('',views.home_page,name="home_page"),
    path('city/Abha/',views.abha_page,name="abha_page"),
    path('city/Riyadh/',views.riyadh_page,name="riyadh_page"),
    path('city/jeddah/',views.jeddah_page,name="jeddah_page"),
    path('city/AlUla/',views.AlUla_page,name="AlUla_page"),
    
]
