from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "accounts"

urlpatterns = [
    # path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("signup_done/", views.signup_done, name="signup_done"),
    path("login/", views.login, name="login"),
    path("login_help/", views.login_help, name="login_help"),
    path("logout/", views.logout, name="logout"),
    path("update/", views.update, name="update"),
    path("password/", views.password, name="password"),
    path("delete/", views.delete, name="delete"),
    path("delete_check/", views.delete_check, name="delete_check"),
    path("<int:user_pk>/detail/", views.detail, name="detail"),
    path("<int:user_pk>/follow/", views.follow, name="follow"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
