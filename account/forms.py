from django.contrib.auth.forms import AuthenticationForm
from django import forms

class UserLogin(AuthenticationForm):
    username = forms.CharField(label="Имя")
    password = forms.CharField(label="Пароль",widget=forms.PasswordInput)
