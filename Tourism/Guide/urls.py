

from django.urls import path
from . import views

app_name = "Guide"

urlpatterns = [
    path("", views.home_page,name="home_page"),
    path("city/al-ula/", views.ula, name="al-ula"),
    path("city/damam/", views.dammam, name="damam"),
    path("city/jeddah/", views.jeddah, name="jeddah"),
    path("city/riyadh/", views.riyadh, name="riyadh")
]