from django.shortcuts import render, redirect
from .models import Book_Review, Book_Review_Comment
from .forms import Book_ReviewForm, Book_Review_CommentForm
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from books.models import Book
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# 책 리뷰 페이지
def index(request):
    if request.GET.get("page"):
        reviews = Book_Review.objects.order_by("-pk")
        page1 = request.GET.get("page", 1)
        totalnum = len(reviews)
        reviews_page = Paginator(reviews, 6)
        totalpagenum = reviews_page.num_pages
        try:
            review_list = reviews_page.page(page1)
        except PageNotAnInteger:
            review_list = reviews_page.page(1)
        except EmptyPage:
            review_list = reviews_page.page(reviews_page.num_pages)
    else:
        reviews = Book_Review.objects.order_by("-pk")
        page1 = request.GET.get("page", 1)
        totalnum = len(reviews)
        reviews_page = Paginator(reviews, 6)
        totalpagenum = reviews_page.num_pages
        try:
            review_list = reviews_page.page(page1)
        except PageNotAnInteger:
            review_list = reviews_page.page(1)
        except EmptyPage:
            review_list = reviews_page.page(reviews_page.num_pages)
        return render(
            request,
            "reviews/index.html",
            {
                "reviews": reviews,
                "review_list": review_list,
                "totalnum": totalnum,
                "totalpagenum": totalpagenum,
            },
        )
    return render(
        request,
        "reviews/index.html",
        {
            "reviews": reviews,
            "review_list": review_list,
            "totalnum": totalnum,
            "totalpagenum": totalpagenum,
        },
    )


# 글 리뷰 작성
@login_required
def create_txt(request, book_pk):
    # 임시 데이터
    bookId = Book.objects.get(pk=book_pk)
    if request.user.is_authenticated:
        if request.method == "POST":
            book_review_form = Book_ReviewForm(request.POST, request.FILES)
            if book_review_form.is_valid():
                book_review = book_review_form.save(commit=False)
                book_review.user = request.user
                book_review.bookId = bookId
                book_review.save()
                book_review_form.save_m2m()
                return redirect(
                    "books:detail",
                    bookId.pk,
                )
        else:
            book_review_form = Book_ReviewForm()
        context = {"book_review_form": book_review_form}
        return render(request, "reviews/create_txt.html", context)


# 사진 리뷰 작성
@login_required
def create_img(request, book_pk):
    # 임시 데이터
    bookId = Book.objects.get(pk=book_pk)
    if request.user.is_authenticated:
        if request.method == "POST":
            book_review_form = Book_ReviewForm(request.POST, request.FILES)
            if book_review_form.is_valid():
                book_review = book_review_form.save(commit=False)
                book_review.user = request.user
                book_review.bookId = bookId
                book_review.save()
                book_review_form.save_m2m()
                return redirect(
                    "books:detail",
                    bookId.pk,
                )
        else:
            book_review_form = Book_ReviewForm()
        context = {"book_review_form": book_review_form}
        return render(request, "reviews/create_img.html", context)


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
        "comments_count": comments.count(),
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
        context = {"book_review_form": book_review_form, "book_review": book_review}

        # 글이 작성되어 있으면(""이 아니면) 글 리뷰 페이지로
        if book_review.content != "":
            return render(request, "reviews/create_txt.html", context)
        # 글이 없으면(=사진이 있으면) 사진 리뷰 페이지로
        else:
            return render(request, "reviews/create_img.html", context)
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
                "userImage": temp.user.user_image(),
                "content": temp.content,
                "commentPk": temp.pk,
                "commentDate": temp.created_at.strftime("%Y-%m-%d"),
            }
        )

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
                "userImage": temp.user.user_image(),
                "content": temp.content,
                "commentPk": temp.pk,
                "commentDate": temp.created_at.strftime("%Y-%m-%d"),
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

@login_required
def pk_create_txt(request):
    book = None
    query = None
    t = request.GET.get("aa")
    try:
        bookId = Book.objects.get(pk=t)

    except Book.DoesNotExist:
        bookId = None

    
    
    if "q" in request.GET:
        query = request.GET.get("q")
        book = Book.objects.order_by("-pk").filter(
            bookname__contains=query
        )

    if request.user.is_authenticated:
        if request.method == "POST":
            book_review_form = Book_ReviewForm(request.POST, request.FILES)
            if book_review_form.is_valid():
                book_review = book_review_form.save(commit=False)
                book_review.user = request.user
                book_review.bookId = bookId
                book_review.save()
                book_review_form.save_m2m()
                return redirect(
                    "books:detail",
                    bookId.pk,
                )
        else:
            book_review_form = Book_ReviewForm()
  
    context = {
        "query": query,
        "book": book,
        "book_review_form": book_review_form,
        "bookId" : bookId,
    }
    return render(request, 'reviews/pk_create_txt.html', context)

@login_required
def pk_create_img(request):
    book = None
    query = None
    t = request.GET.get("aa")
    try:
        bookId = Book.objects.get(pk=t)

    except Book.DoesNotExist:
        bookId = None

    
    
    if "q" in request.GET:
        query = request.GET.get("q")
        book = Book.objects.order_by("-pk").filter(
            bookname__contains=query
        )

    if request.user.is_authenticated:
        if request.method == "POST":
            book_review_form = Book_ReviewForm(request.POST, request.FILES)
            if book_review_form.is_valid():
                book_review = book_review_form.save(commit=False)
                book_review.user = request.user
                book_review.bookId = bookId
                book_review.save()
                book_review_form.save_m2m()
                return redirect(
                    "books:detail",
                    bookId.pk,
                )
        else:
            book_review_form = Book_ReviewForm()
  
    context = {
        "query": query,
        "book": book,
        "book_review_form": book_review_form,
        "bookId" : bookId,
    }
    return render(request, 'reviews/pk_create_img.html', context)