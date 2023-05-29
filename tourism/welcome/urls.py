from django.urls import path
from . import views

app_name="welcome"

urlpatterns =[

    path("", views.home_page, name='home_page'),

     path("", views.Al-ahsa_page, name='Al-ahsa_page'),

      path("", views.A-ola_page, name='Al-ola_page'),

       path("", views.Riyadh_page, name='Riyadh_page'),

        path("", views.Jeedah_page, name='Jeedah_page')

]