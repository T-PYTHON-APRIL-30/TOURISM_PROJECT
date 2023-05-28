from django.urls import path
from . import views

app_name = 'tourism_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('city/', views.city, name='city'),
    path('riyadh/',views.riyadh,name='riyadh'),
    path('city/abha/',views.abha,name='abha'),
    path('city/makkah/',views.makkah,name='makkah'),
    path('city/alula/',views.alula,name='alula'),

]

