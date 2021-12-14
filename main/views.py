from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from users_1c.models import ListUsers

def main(request):
    if not request.user.is_authenticated:
        return redirect('/')
    
    user_1c = ListUsers.objects.get(user_web=request.user)

    return render(request, 'main/main.html', context={"user":request.user,
        "role":user_1c.user_role,
        "title":"Главная"})
