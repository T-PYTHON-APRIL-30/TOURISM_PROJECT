from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.home_page, name = 'home'),
    path('/riyadh', views.riyadh, name='riyadhh'),
    path('/abha', views.abha, name='abha'),
    path('/mekkah', views.mekkah, name = 'mekkah'),
    path('/almadinah', views.almadinah, name = 'almadinah'),
]