from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)

def user_login(request):
    form = LoginForm(request, data=request.POST)
    if form.is_valid():
        form.save()
        user = form.get_user()
        login(request, user)
        messages.success("You are now logged in")
        return redirect('home')
    
    context = {
        'form': form,
    }
    return render(request, 'users/login.html')