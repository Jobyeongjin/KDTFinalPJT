from django import forms
from .models import Book, Book_Review, Book_Review_Comment

class Book_ReviewForm(forms.ModelForm):
    class Meta:
        model = Book_Review
        fields = [
            "content",
            "image",
        ]

class Book_Review_CommentForm(forms.ModelForm):
    class Meta:
        model = Book_Review_Comment
        fields = ["content"]