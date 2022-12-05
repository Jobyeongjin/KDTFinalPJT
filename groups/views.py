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

# 모임 디테일
def detail(request, pk):
    group = Group.objects.get(pk=pk)
    place = group.place
    context = {
        "group":group,
        "place":place,
    }
    return render(request, "groups/detail.html", context)

# 모임 업데이트
@login_required
def update(request, pk):
    group = Group.objects.get(pk=pk)
    if request.user == group.user:
        if request.method == "POST":
            group_form = GroupForm(request.POST, request.FILES, instance=group)
            if group_form.is_valid():
                group_form.save()
                return redirect("groups:detail", pk)
        else:
            group_form = GroupForm(instance=group)
        context = {"group_form": group_form}
        return render(request, "groups/create.html", context)
    else:
        return HttpResponseForbidden()

# 모임 삭제
@login_required
def delete(request, pk):
    group = Group.objects.get(pk=pk)
    if request.user == group.user:
        group.delete()
        return redirect("groups:index")
    else:
        return HttpResponseForbidden()