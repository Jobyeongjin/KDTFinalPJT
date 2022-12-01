from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth import get_user_model


class CustomCreationUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "interest"]
        labels = {"username": "이름", "interest": "관심분야"}


class CustonChangeUserForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = [
            "nickname",
            "email",
            "age",
            "username",
            "profile_image",
            "status_message",
        ]
        labels = {
            "nickname": "닉네임",
            "username": "이름",
            "email": "이메일",
            "profile_image": "프로필 사진",
            "status_message": "상태 메세지",
        }
