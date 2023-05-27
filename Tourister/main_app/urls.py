from django.urls import path
from . import views

app_name = 'main_app'


urlpatterns =[
   
    path("", views.home_page, name='home_page'),
    path("contact", views.contact_page, name='contact_page'),
    path("city/makkah", views.makkah_page, name='makkah_page'),
    path("city/riyadh", views.riyadh_page, name='riyadh_page'),
    path("city/alula", views.alula_page, name='alula_page'),
    path("city/jeddah", views.jeddah_page, name='jeddah_page'),

]