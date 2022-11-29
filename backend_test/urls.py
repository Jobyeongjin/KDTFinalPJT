from django.urls import path
from . import views

app_name = 'backend_test'

urlpatterns = [
    path("", views.index, name="index"),
]
