from django.shortcuts import render, redirect
from .forms import NoticeForm
from .models import Notice
from django.http import HttpResponseForbidden


def index(request):
    notices = Notice.objects.order_by("-pk")
    return render(
        request,
        "notices/index.html",
        {
            "notices": notices,
        },
    )


# 슈퍼 유저일 경우에만
def create(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = NoticeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("notices:index")
        else:
            form = NoticeForm()
        return render(
            request,
            "notices/create.html",
            {
                "form": form,
            },
        )
    else:
        return HttpResponseForbidden()


def detail(request, pk):
    notice = Notice.objects.get(pk=pk)
    return render(
        request,
        "notices/detail.html",
        {
            "notice": notice,
        },
    )


# 슈퍼 유저일 경우에만
def update(request, pk):
    notice = Notice.objects.get(pk=pk)
    if request.user.is_superuser:
        if request.method == "POST":
            form = NoticeForm(request.POST, instance=notice)
            if form.is_valid():
                form.save()
                return redirect("notices:detail", pk)
        else:
            form = NoticeForm(instance=notice)
        return render(
            request,
            "notices/update.html",
            {
                "form": form,
                "notice": notice,
            },
        )
    else:
        return HttpResponseForbidden()


# 슈퍼 유저일 경우에만
def delete(request, pk):
    notice = Notice.objects.get(pk=pk)
    if request.user.is_superuser:
        notice.delete()
        return redirect("notices:index")
    else:
        return HttpResponseForbidden()
