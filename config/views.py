from books.models import Book
from django.shortcuts import render


def nav(request):
    books = Book.objects.all()
    context = {
        "books" : books
    }
    return render(request, "nav.html", context)