from django.urls import path
from . import views

app_name = "groups"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>/detail/", views.detail, name="detail"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/like/", views.like, name="like"),
    path("<int:pk>/group_closed/", views.group_closed, name="group_closed"),
]
