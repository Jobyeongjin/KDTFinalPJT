from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>/detail/", views.detail, name="detail"),
    path("<int:pk>/like/", views.like, name="like"),
    path("<int:pk>/update", views.update, name="update"),
    path("<int:pk>/delete", views.delete, name="delete"),
    path(
        "<int:review_pk>/comment_create/", views.comment_create, name="comment_create"
    ),
    path(
        "comment_delete/<int:comment_pk>/",
        views.comment_delete,
        name="comment_delete",
    ),
]
