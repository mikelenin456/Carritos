from django.urls import path

from .views import login_page, logout_page, VendedorCreateView, VendedorListView

urlpatterns = [
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('create-vendedor/', VendedorCreateView.as_view(), name='create-vendedor'),
    path('list-vendedor/', VendedorListView.as_view(), name='list-vendedor'),
]
