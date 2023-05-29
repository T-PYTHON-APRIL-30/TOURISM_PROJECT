from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("", views.home, name = "home"),
    path('city/Alula/', views.alula, name='alula'),
    path('city/Riyadh', views.riyadh, name='riyadh'),
    path('city/Mecca', views.mecca, name='mecca'),
    path('city/Dhahran', views.dhahran, name='dhahran'),
]