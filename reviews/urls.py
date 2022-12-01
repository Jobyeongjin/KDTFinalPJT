from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.review, name="review"),
    path("create/", views.create, name="create"),
    path("<int:pk>/detail/", views.detail, name="detail"),
    path("<int:pk>/review_update", views.update, name="update"),
    path("<int:pk>/review_delete", views.delete, name="delete"),
    path("<int:pk>/comment/create/", views.comment_create, name="comment_create"),

]
