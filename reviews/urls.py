from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:book_pk>/create_txt/", views.create_txt, name="create_txt"),
    path("<int:book_pk>/create_img/", views.create_img, name="create_img"),
    path("<int:pk>/detail/", views.detail, name="detail"),
    path("<int:pk>/update", views.update, name="update"),
    path("<int:pk>/delete", views.delete, name="delete"),
    path("<int:pk>/like/", views.like, name="like"),
    path(
        "<int:review_pk>/comment_create/", views.comment_create, name="comment_create"
    ),
    path(
        "comment_delete/<int:comment_pk>/",
        views.comment_delete,
        name="comment_delete",
    ),
    path("pk_create_txt/", views.pk_create_txt, name="pk_create_txt"),
    path("pk_create_img/", views.pk_create_img, name="pk_create_img"),
]
