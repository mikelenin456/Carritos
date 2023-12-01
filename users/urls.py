from django.urls import path

from .views import login_page, logout_page, create_vendedor, VendedorListView, delete_vendedor

urlpatterns = [
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('create-vendedor/', create_vendedor, name='create-vendedor'),
    path('list-vendedor/', VendedorListView.as_view(), name='list-vendedor'),
    path('delete-vendedor/<int:pk>/', delete_vendedor, name='delete-vendedor'),
]
