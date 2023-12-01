from django import forms
from users.models import User
from typing import Any


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Username",
            }
        )
    )
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
                "type": "password",
            }
        )
    )


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password"]

        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control", 
                    "placeholder": "Nombre"}
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control", 
                    "placeholder": "Apellidos"}
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email",
                }
            ),
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Usuario",
                }
            ),
            "password": forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Contraseña",
                }
            ),
        }
