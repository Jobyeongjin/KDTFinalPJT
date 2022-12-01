from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import CustomCreationUserForm, CustonChangeUserForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def index(request):
    users = get_user_model().objects.all()
    context = {"users": users}
    return render(request, "accounts/index.html", context)


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
            return redirect("accounts:index")
    else:
        form = AuthenticationForm()
    context = {"form": form}

    return render(request, "accounts/login.html", context)


# 로그아웃
def logout(request):
    auth_logout(request)
    return redirect("accounts:index")


# 회원 정보 수정
def update(request):
    if request.method == "POST":
        form = CustonChangeUserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:index")

    else:
        form = CustonChangeUserForm(instance=request.user)

    context = {"form": form}

    return render(request, "accounts/update.html", context)


# 회원 탈퇴
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect("accounts:signup")


# 회원 정보
def detail(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)

    context = {"user": user}

    return render(request, "accounts/detail.html", context)
