from django import forms
from .models import Group

class DateInput(forms.DateInput):
    input_type = "date"

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            "place",
            "number",
            "meeting_date",
            "end_date",
            "image",
        ]
        widgets = {
            "meeting_date": DateInput(),
            "end_date":DateInput(),
        }