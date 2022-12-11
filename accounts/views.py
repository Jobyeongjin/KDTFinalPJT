from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .forms import CustomCreationUserForm, CustonChangeUserForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout, authenticate
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from datetime import datetime
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from books.models import Book

# Create your views here.
# def index(request):
#     users = get_user_model().objects.all()
#     context = {"users": users}
#     return render(request, "accounts/index.html", context)


# 회원가입
def signup(request):
    if request.method == "POST":
        form = CustomCreationUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect("accounts:signup_done")
    else:
        form = CustomCreationUserForm()

    context = {"form": form}

    return render(request, "accounts/signup.html", context)


# 회원가입 완료
def signup_done(request):
    return render(request, "accounts/signup_done.html")


# 로그인
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("books:main")
    else:
        form = AuthenticationForm()
    context = {"form": form}

    return render(request, "accounts/login.html", context)


# 로그인 도움말
def login_help(request):
    return render(request, "accounts/login_help.html")


# 로그아웃
def logout(request):
    auth_logout(request)
    return redirect("books:main")


# 회원 정보 수정
@login_required
def update(request):
    user = get_user_model().objects.get(pk=request.user.pk)
    if request.method == "POST":
        form = CustonChangeUserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:detail", user.pk)

    else:
        form = CustonChangeUserForm(instance=request.user)

    context = {"form": form, "user": user}

    return render(request, "accounts/update.html", context)


# 회원 비밀번호 변경
@login_required
def password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # 로그인 유지
            return redirect("accounts:login")

    else:
        form = PasswordChangeForm(request.user)

    context = {
        "form": form,
    }

    return render(request, "accounts/password.html", context)


# 회원 탈퇴
@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect("books:main")


# 회원 탈퇴 체크
def delete_check(request):
    user = get_user_model().objects.get(pk=request.user.pk)
    today = datetime.date(datetime.now())
    date_joined = datetime.date(user.date_joined)
    diff = (today - date_joined).days + 1
    reviews = user.book_review_set.count
    user_groups = user.group_set.count
    context = {
        "user": user,
        "diff": diff,
        "reviews": reviews,
        "user_groups": user_groups,
    }
    return render(request, "accounts/delete.html", context)


# 회원 정보
def detail(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    book_likes = user.books.all()
    user_reviews = user.book_review_set.order_by("-pk")
    user_like_reviews = user.like_review.order_by("-pk")
    user_groups = user.group_set.order_by("-pk")
    user_like_groups = user.like_group.order_by("-pk")
    context = {
        "user": user,
        "book_likes": book_likes,
        "user_reviews": user_reviews,
        "user_like_reviews": user_like_reviews,
        "user_groups": user_groups,
        "user_like_groups": user_like_groups,
    }

    return render(request, "accounts/detail.html", context)


# 팔로우
@login_required
def follow(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    if request.user != get_user_model().objects.get(pk=user_pk):
        if user.followers.filter(pk=request.user.pk).exists():
            user.followers.remove(request.user)
            is_followed = False
        else:
            user.followers.add(request.user)
            is_followed = True
        context = {
            "is_followed": is_followed,
            "followers_count": user.followers.count(),
            "followings_count": user.followings.count(),
        }
        return JsonResponse(context)
