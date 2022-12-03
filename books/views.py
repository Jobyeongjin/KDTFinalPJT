from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Count
from urllib import parse


def onboarding(request):
    return render(request, "books/onboarding.html")


# 메인 페이지
def main(request):
    books = Book.objects.all().annotate(hot=Count("like_user")).order_by("-hot")

    return render(
        request,
        "books/main.html",
        {
            "books": books[:4],
        },
    )


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
def detail(request, pk):
    book = Book.objects.get(pk=pk)
    book_url = parse.quote(book.bookname)
    context = {
        "book": book,
        "book_url": book_url,
    }
    return render(request, "books/book_detail.html", context)


def like(request, book_pk):
    if request.user.is_authenticated:
        book = Book.objects.get(pk=book_pk)

        if book.like_user.filter(pk=request.user.pk).exists():
            book.like_user.remove(request.user)
            is_liked = False
        else:
            book.like_user.add(request.user)
            is_liked = True
    context = {
        "is_liked": is_liked,
        "like_count": book.like_user.count(),
    }

    return JsonResponse(context)
