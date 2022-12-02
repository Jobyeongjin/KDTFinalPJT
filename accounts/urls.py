from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("signupdone/", views.signup_done, name="signup_done"),
    path("login/", views.login, name="login"),
    path("loginhelp/", views.login_help, name="login_help"),
    path("logout/", views.logout, name="logout"),
    path("update/", views.update, name="update"),
    path("password/", views.password, name="password"),
    path("delete/", views.delete, name="delete"),
    path("deletecheck/", views.delete_check, name="delete_check"),
    path("<int:user_pk>/detail/", views.detail, name="detail"),
    path("<int:user_pk>/follow/", views.follow, name="follow"),
    # detail test
    path("<int:user_pk>/detail_test/", views.detail_test, name="detail_test"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
