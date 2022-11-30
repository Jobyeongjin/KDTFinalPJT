from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/book_detail/", views.book_detail, name="book_detail"),
    path("review/",views.review, name="review"),
    path("create/", views.create, name="create"),
    path("<int:pk>/review_detail/", views.review_detail, name="review_detail"),
    path("<int:pk>/review_update", views.update, name="update"),
    path("<int:pk>/review_delete", views.delete, name="delete"),
]
