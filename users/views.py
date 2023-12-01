from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

from users.forms import UserForm
from users.models import User
from .forms import LoginForm
from users.services.user_service import UserService
from users.enums import Groups

def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    context = {'form': forms}
    return render(request, 'users/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')


class VendedorCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = "users/add_vendedor.html"
    success_url = reverse_lazy("list-vendedor")

    def form_valid(self, form):
        _ = UserService.create_vendedor(form.cleaned_data)
        return redirect(self.success_url)

class VendedorListView(ListView):
    model = User
    template_name = 'users/vendedor_list.html'
    context_object_name = 'vendedores'

    def get_queryset(self):
        return User.objects.filter(groups__name=Groups.VENDEDOR.value)

