from django.urls import path
from . import views

app_name = 'backend_test'

urlpatterns = [
    path("", views.index, name="index"),
    path("map/", views.map, name="map"),
    path("map2/", views.map2, name="map2"),

]
