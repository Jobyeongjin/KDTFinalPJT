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
    path("logout/", views.logout, name="logout"),
    path("update/", views.update, name="update"),
    path("delete/", views.delete, name="delete"),
    path("<int:user_pk>/detail/", views.detail, name="detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
