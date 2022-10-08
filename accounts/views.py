from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from . forms import * 
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']

            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password, email=email)
            user.save()
            messages.success(request, 'You are now registered and can log in')
            return redirect(signin)

    else:
        form = Register()
    return render(request, 'accounts/register.html',{"form": form})

def signin(request):
    if request.method == 'POST':
        form = Signin(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, 'You are now logged in')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('login')
    else:
        form = Signin()
        return render(request, 'accounts/login.html', {"form": form})