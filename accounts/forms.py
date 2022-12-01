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
            "profile_image",
            "status_message",
            "interest",
        ]
        labels = {
            "nickname": "닉네임",
            "email": "이메일",
            "age": "나이",
            "profile_image": "프로필 사진",
            "status_message": "상태 메세지",
            "interest": "관심분야",
        }
