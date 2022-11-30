from django.shortcuts import render
from .models import Book

def onboarding(request):
    return render(request, "books/onboarding.html")

def index(request):
    books = Book.objects.all()
    return render(
        request,
        "books/index.html",
        {
            "books": books,
        },
    )
