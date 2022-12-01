from django.shortcuts import render, redirect
from .models import Book, Book_Review, Book_Review_Comment
from .forms import Book_ReviewForm, Book_Review_CommentForm
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
            "books": books[:10],
        },
    )


# 책 디테일 페이지(댓글추가전)
def book_detail(request, pk):
    book = Book.objects.get(pk=pk)

    context = {
        "book": book,
    }
    return render(request, "books/book_detail.html", context)


# 책 리뷰 페이지
def review(request):
    book_reviews = Book_Review.objects.all()

    context = {
        "book_reviews": book_reviews,
    }
    return render(request, "books/review.html", context)


# 책 리뷰 작성
@login_required
def create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            book_review_form = Book_ReviewForm(request.POST, request.FILES)
            if book_review_form.is_valid():
                book_review = book_review_form.save(commit=False)
                book_review.user = request.user
                book_review.save()
                return redirect("books:review")
        else:
            book_review_form = Book_ReviewForm()
        context = {"book_review_form": book_review_form}
        return render(request, "books/create.html", context)


# 책 리뷰 디테일(댓글 추가 전)
def review_detail(request, pk):
    book_review = Book_Review.objects.get(pk=pk)

    context = {
        "book_review": book_review,
    }
    return render(request, "books/review_detail.html", context)


# 리뷰 업데이트
@login_required
def update(request, pk):
    book_review = Book_Review.objects.get(pk=pk)
    if request.user == book_review.user:
        if request.method == "POST":
            book_review_form = Book_ReviewForm(request.POST, request.FILES, instance=book_review)
            if book_review_form.is_valid():
                book_review_form.save()
                return redirect("books:review_detail", pk)
        else:
            book_review_form = Book_ReviewForm(instance=book_review)
        context = {"book_review_form": book_review_form}
        return render(request, "books/create.html", context)
    else:
        return HttpResponseForbidden()


# 리뷰 삭제
@login_required
def delete(request, pk):
    book_review = Book_Review.objects.get(pk=pk)
    if request.user == book_review.user:
        book_review.delete()
        return redirect("books:review")
    else:
        return HttpResponseForbidden()


