from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.index, name="index"),
    path("review/",views.review, name="review"),
    path("create/", views.create, name="create"),
    path("<int:pk>/review_detail/", views.review_detail, name="review_detail"),
]
