from django.shortcuts import render, redirect
from .models import Book_Review, Book_Review_Comment
from .forms import Book_ReviewForm, Book_Review_CommentForm
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from books.models import Book
from django.http import JsonResponse

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
                return redirect(
                    "books:detail",
                    bookId.pk,
                )
        else:
            book_review_form = Book_ReviewForm()
        context = {"book_review_form": book_review_form}
        return render(request, "reviews/create.html", context)


# 책 리뷰 디테일(댓글 추가 전)
def detail(request, pk):
    review = Book_Review.objects.get(pk=pk)
    bookId = review.bookId
    like_count = review.like_user.count()
    comments = Book_Review_Comment.objects.filter(book_review=review).order_by("-pk")
    review_like_user = review.like_user
    review_user_follwers = review.user.followers.all
    comment_form = Book_Review_CommentForm()
    context = {
        "review": review,
        "book": bookId,
        "like_count": like_count,
        "comments": comments,
        "comment_form": comment_form,
        "review_like_user": review_like_user,
        "review_user_follwers": review_user_follwers,
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
def comment_create(request, review_pk):
    print(request.POST)
    book_review = Book_Review.objects.get(pk=review_pk)
    comment_form = Book_Review_CommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.book_review = book_review
        comment.user = request.user
        comment.save()

    user = request.user.pk
    data = Book_Review_Comment.objects.filter(book_review_id=review_pk).order_by("-pk")
    comment_data = []

    for temp in data:
        comment_data.append(
            {
                "user_pk": temp.user_id,
                "userName": temp.user.username,
                "content": temp.content,
                "commentPk": temp.pk,
                "commentDate": temp.created_at.strftime("%y.%m.%d"),
            }
        )

    print("여기까지 실행")
    return JsonResponse(
        {
            "comment_data": comment_data,
            "review_pk": book_review.pk,
            "user": user,
        },
    )


@login_required
def comment_delete(request, comment_pk):
    comment = Book_Review_Comment.objects.get(pk=comment_pk)
    book_review = comment.book_review
    comment.delete()

    user = request.user.pk
    data = Book_Review_Comment.objects.filter(book_review_id=book_review).order_by(
        "-pk"
    )
    comment_data = []

    for temp in data:
        comment_data.append(
            {
                "user_pk": temp.user_id,
                "userName": temp.user.username,
                "content": temp.content,
                "commentPk": temp.pk,
                "commentDate": temp.created_at.strftime("%y.%m.%d"),
            }
        )
    return JsonResponse(
        {
            "comment_data": comment_data,
            "review_pk": book_review.pk,
            "user": user,
        }
    )


# 리뷰 좋아요
def like(request, pk):
    if request.user.is_authenticated:
        review = Book_Review.objects.get(pk=pk)
        if review.like_user.filter(pk=request.user.pk).exists():
            review.like_user.remove(request.user)
            is_liked = False
        else:
            review.like_user.add(request.user)
            is_liked = True
    else:
        return redirect("reviews:detail", pk)
    return JsonResponse(
        {
            "is_liked": is_liked,
            "like_count": review.like_user.count(),
        }
    )
