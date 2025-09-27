from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

def register(response):

    if response.method == 'POST':
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("index")
    
    else:
        form = UserCreationForm
    
        return render(response, 'register/register.html', {'form':form})

class LoginInterfaceView(LoginView):
    template_name = 'notes/base.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'register/registration/logout.html'