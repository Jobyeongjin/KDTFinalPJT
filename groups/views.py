from django.shortcuts import render, redirect
from .models import Group
from .forms import GroupForm
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

# Create your views here.


# 모임 페이지
def index(request):
    groups = Group.objects.all()
    context = {
        "groups":groups,
    }
    return render(request, "groups/index.html",context)


# 모임 생성
@login_required
def create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            group_form = GroupForm(request.POST, request.FILES)
            if group_form.is_valid():
                book_review = group_form.save(commit=False)
                book_review.user = request.user
                book_review.save()
                return redirect("groups:index")
        else:
            group_form = GroupForm()
        context = {"group_form": group_form}
        return render(request, "groups/create.html", context)

# 책 리뷰 디테일(댓글 추가 전)
def detail(request, pk):
    group = Group.objects.get(pk=pk)
    context = {
        "group":group,
    }
    return render(request, "groups/detail.html", context)