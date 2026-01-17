from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import User


class UserListView(ListView):
    model = User
    template_name = "users/list.html"
    context_object_name = "users"


class UserDetailView(DetailView):
    model = User
    template_name = "users/detail.html"
    context_object_name = "user"


class UserCreateView(CreateView):
    model = User
    fields = ["username", "email", "is_active"]
    template_name = "users/form.html"
    success_url = reverse_lazy("users:list")


class UserUpdateView(UpdateView):
    model = User
    fields = ["username", "email", "is_active"]
    template_name = "users/form.html"
    success_url = reverse_lazy("users:list")


class UserDeleteView(DeleteView):
    model = User
    template_name = "users/delete.html"
    success_url = reverse_lazy("users:list")
