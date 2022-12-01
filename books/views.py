from django.shortcuts import render, redirect
from .models import Book
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required


def onboarding(request):
    return render(request, "books/onboarding.html")


# 메인 페이지
def main(request):
    return render(request, "books/main.html")


# 책 리스트 페이지
def index(request):
    books = Book.objects.all()
    return render(
        request,
        "books/index.html",
        {
            "books": books,
        },
    )


# 책 디테일 페이지(댓글추가전)
def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        "book": book,
    }
    return render(request, "books/book_detail.html", context)



