from django.urls import path
from . import views

app_name = 'visit_saudi'

urlpatterns = [
    path('',views.home,name='home_page'),
    path('city/riyadh',views.riyadh,name='riyadh'),
    path('city/abha',views.abha,name='abha'),
    path('city/mekkah',views.mekkah,name='mekkah'),
    path('city/AlUla',views.alula,name='alula')
]
