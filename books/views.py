from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Count
from urllib import parse
from django.db.models import Q
from accounts.models import User
from books.models import Book
from reviews.models import Book_Review
from groups.models import Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag


def onboarding(request):
    books = Book.objects.all().annotate(hot=Count("like_user")).order_by("-hot")
    reviews = Book_Review.objects.annotate(hot=Count("like_user")).order_by("-hot")

    return render(
        request,
        "books/onboarding.html",
        {
            "books": books,
            "reviews": reviews,
        },
    )


# 메인 페이지
def main(request):
    books = Book.objects.all().annotate(hot=Count("like_user")).order_by("-hot")
    reviews = Book_Review.objects.annotate(hot=Count("like_user")).order_by("-hot")
    groups = Group.objects.filter(closed=0).order_by("-pk")

    return render(
        request,
        "books/main.html",
        {
            "books": books[:4],
            "reviews": reviews[:3],
            "book_reviews_carousel": reviews[:10],
            "groups": groups[:3],
        },
    )


# 책 리스트 페이지
def index(request):
    if request.GET.get("page"):
        books = Book.objects.all()
        page1 = request.GET.get("page", 1)
        totalnum = len(books)
        books_page = Paginator(books, 20)
        totalpagenum = books_page.num_pages
        try:
            book_list = books_page.page(page1)
        except PageNotAnInteger:
            book_list = books_page.page(1)
        except EmptyPage:
            book_list = books_page.page(books_page.num_pages)

    else:
        books = Book.objects.all()
        page1 = request.GET.get("page", 1)
        totalnum = len(books)
        books_page = Paginator(books, 20)
        totalpagenum = books_page.num_pages
        try:
            book_list = books_page.page(page1)
        except PageNotAnInteger:
            book_list = books_page.page(1)
        except EmptyPage:
            book_list = books_page.page(books_page.num_pages)

    count = Book.objects.all().count()

    return render(
        request,
        "books/index.html",
        {
            "books": books,
            "book_list": book_list,
            "totalnum": totalnum,
            "totalpagenum": totalpagenum,
            "count": count,
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
        "book_reviews_carousel": book_reviews[:10],
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


# navbar search 기능
def search(request):
    book = None
    user = None
    query = None
    reviews = None
    authors = None
    tags = None
    if "search" in request.GET:
        query = request.GET.get("search")
        book = Book.objects.order_by("-pk").filter(bookname__contains=query)
        authors = Book.objects.order_by("-pk").filter(authors__contains=query)
        user = User.objects.order_by("-pk").filter(nickname__contains=query)
        reviews = Book_Review.objects.filter(content__contains=query)
        tags = Tag.objects.filter(name__contains=query)
        tags_review = Book_Review.objects.filter(tags__name__contains=query)

    context = {
        "query": query,
        "books": book,
        "user": user,
        "reviews": reviews,
        "authors": authors,
        "tags": tags,
        "tags_review": tags_review,
    }

    return render(request, "books/search.html", context)
