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
    book_reviews = book.book_review_set.order_by("-pk")
    context = {
        "book": book,
        "book_url": book_url,
        "book_reviews": book_reviews,
        "book_reviews_writer": book_reviews[:8],
        "book_reviews_carousel": book_reviews[:6],
    }
    return render(request, "books/book_detail.html", context)


def like(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    if request.user in book.like_user.all():
        book.like_user.remove(request.user)
        is_liked = False
    else:
        book.like_user.add(request.user)
        is_liked = True
    context = {
        "isLiked": is_liked,
        "like_count": book.like_user.count(),
    }

    return JsonResponse(context)
