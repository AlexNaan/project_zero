from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserLogin

def user_login(request):
    
    if request.user.is_authenticated:
        return redirect('main')

    if request.method == 'POST':
        form = UserLogin(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)

            return redirect('main')
        else:
            form = UserLogin()
            return render(request, 'account/login.html', {'form': form})
    else:
        form = UserLogin()
        return render(request, 'account/login.html', {'form': form})


def user_exit(request):
   
    logout(request)
    return redirect('/')
