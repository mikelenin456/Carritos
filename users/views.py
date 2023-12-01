from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest

from users.forms import UserForm
from users.models import User
from .forms import LoginForm
from users.services.user_service import UserService
from users.enums import Groups


def login_page(request):
    forms = LoginForm()
    if request.method == "POST":
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data["username"]
            password = forms.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("dashboard")
    context = {"form": forms}
    return render(request, "users/login.html", context)


def logout_page(request):
    logout(request)
    return redirect("login")


class VendedorListView(ListView):
    model = User
    template_name = "users/vendedor_list.html"
    context_object_name = "vendedores"

    def get_queryset(self):
        return User.objects.filter(groups__name=Groups.VENDEDOR.value)


@login_required(login_url="login")
def create_vendedor(request: HttpRequest):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            UserService.create_vendedor(form.cleaned_data)
            return redirect("list-vendedor")
    context = {"form": form}
    return render(request, "users/add_vendedor.html", context)

@login_required(login_url="login")
def delete_vendedor(request: HttpRequest, pk: int):
    user = get_object_or_404(User, pk=pk)
    UserService.delete_vendedor(user)
    return redirect("list-vendedor")
