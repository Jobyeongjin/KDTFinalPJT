from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.index, name="index"),
    path("onboarding/", views.onboarding, name="onboarding"),
    path("main/", views.main, name="main"),
    path("<int:pk>/book_detail/", views.book_detail, name="book_detail"),
]
