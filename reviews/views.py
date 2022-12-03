from django.shortcuts import render, redirect
from .models import Book_Review, Book_Review_Comment
from .forms import Book_ReviewForm, Book_Review_CommentForm
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from books.models import Book

# Create your views here.


# 책 리뷰 페이지
def index(request):
    reviews = Book_Review.objects.order_by("-pk")

    context = {
        "reviews": reviews,
    }
    return render(request, "reviews/index.html", context)


# 책 리뷰 작성
@login_required
def create(request):
    # 임시 데이터
    bookId = Book.objects.get(pk=1)
    if request.user.is_authenticated:
        if request.method == "POST":
            book_review_form = Book_ReviewForm(request.POST, request.FILES)
            if book_review_form.is_valid():
                book_review = book_review_form.save(commit=False)
                book_review.user = request.user
                book_review.bookId = bookId
                book_review.save()
                return redirect("books:detail", bookId.pk)
        else:
            book_review_form = Book_ReviewForm()
        context = {"book_review_form": book_review_form}
        return render(request, "reviews/create.html", context)


# 책 리뷰 디테일(댓글 추가 전)
def detail(request, pk):
    book_review = Book_Review.objects.get(pk=pk)
    comments = book_review.book_review_comment_set.all()
    comment_form = Book_Review_CommentForm()
    context = {
        "book_review": book_review,
        "comments": comments,
        "comment_form": comment_form,
    }
    return render(request, "reviews/detail.html", context)


# 리뷰 업데이트
@login_required
def update(request, pk):
    book_review = Book_Review.objects.get(pk=pk)
    if request.user == book_review.user:
        if request.method == "POST":
            book_review_form = Book_ReviewForm(
                request.POST, request.FILES, instance=book_review
            )
            if book_review_form.is_valid():
                book_review_form.save()
                return redirect("reviews:detail", pk)
        else:
            book_review_form = Book_ReviewForm(instance=book_review)
        context = {"book_review_form": book_review_form}
        return render(request, "reviews/create.html", context)
    else:
        return HttpResponseForbidden()


# 리뷰 삭제
@login_required
def delete(request, pk):
    book_review = Book_Review.objects.get(pk=pk)
    if request.user == book_review.user:
        book_review.delete()
        return redirect("reviews:index")
    else:
        return HttpResponseForbidden()


# 댓글 추가
@login_required
def comment_create(request, pk):
    book_review = Book_Review.objects.get(pk=pk)
    comment_form = Book_Review_CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.book_review = book_review
        comment.user = request.user
        comment.save()
        return redirect("reviews:detail", pk)


@login_required
def comment_delete(request, review_pk, comment_pk):
    book_review = Book_Review.objects.get(pk=review_pk)
    comment = Book_Review_Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
        return redirect("reviews:detail", book_review.pk)
    else:
        return HttpResponseForbidden()
