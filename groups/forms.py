from django import forms
from .models import Group


class DateInput(forms.DateInput):
    input_type = "date"


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            "title",
            "introduce",
            "place",
            "number",
            "meeting_date",
            "end_date",
            "image",
            "closed",
        ]

        labels = {
            "title": "모임 제목",
            "introduce": "소개글",
            "place": "주소",
            "number": "모집인원",
            "meeting_date": "모임날짜",
            "end_date": "마감일",
            "image": "이미지",
            "closed": "마감버튼",
        }
        widgets = {
            "meeting_date": DateInput(),
            "end_date": DateInput(),
        }
