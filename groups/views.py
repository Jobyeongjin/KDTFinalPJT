from django.shortcuts import render, redirect
from .models import Group
from .forms import GroupForm
from django.http import JsonResponse
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

# Create your views here.

# 모임 페이지
def index(request):
    groups = Group.objects.order_by("-pk")
    ing_groups = Group.objects.filter(closed=0)
    end_groups = Group.objects.filter(closed=1)
    context = {
        "groups": groups,
        "ing_groups": ing_groups,
        "end_groups": end_groups,
    }
    return render(request, "groups/index.html", context)


# 모임 생성
@login_required
def create(request):
    print(request.POST)
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
    like_count = group.like_user.count()
    group_like_user = group.like_user
    if like_count >= group.number:
        group.closed = True
        group.save()

    context = {
        "group": group,
        "place": place,
        "like_count": like_count,
        "group_like_user": group_like_user,
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
        context = {
            "group_form": group_form,
            "group": group,
        }
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


# 모집 신청
@login_required
def like(request, pk):
    if request.user.is_authenticated:
        group = Group.objects.get(pk=pk)
        if group.like_user.filter(pk=request.user.pk).exists():
            group.like_user.remove(request.user)
            is_liked = False
        else:
            group.like_user.add(request.user)
            is_liked = True
    else:
        return redirect("groups:detail", pk)
    context = {
        "is_liked": is_liked,
        "like_count": group.like_user.count(),
    }

    return JsonResponse(context)


# 모집마감
def group_closed(request, pk):
    if request.user.is_authenticated:
        group = Group.objects.get(pk=pk)
        if group.closed == False:
            group.closed = True
            group.save()
        else:
            group.closed = False
            group.save()
        return redirect("groups:detail", pk)
    else:
        return redirect("groups:detail", pk)
