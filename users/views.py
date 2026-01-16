from django.shortcuts import get_object_or_404, redirect, render

from .forms import UserForm
from .models import User


def user_list(request):
    users = User.objects.all()
    return render(request, "users/list.html", {"users": users})


def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, "users/detail.html", {"user": user})


def user_create(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("users:list")

    return render(request, "users/form.html", {"form": form})


def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = UserForm(request.POST or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect("users:list")

    return render(request, "users/form.html", {"form": form})


def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        user.delete()
        return redirect("users:list")

    return render(request, "users/delete.html", {"user": user})
