from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.onboarding, name="onboarding"),
    path("main/", views.main, name="main"),
    path("books/", views.index, name="index"),
    path("books/<int:pk>/detail/", views.detail, name="detail"),
    path("books/<int:book_pk>/like/", views.like, name="like"),
    path("search/", views.search, name="search"),
]
