from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import *


# Create your views here.


def register(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            password2 = request.POST["password2"]

            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password,
                email=email,
            )
            user.save()
            messages.success(request, "Account Created successfully for " + username)
            return redirect(signin)
    else:
        form = Register()
    return render(request, "accounts/register.html", {"form": form})


def signin(request):
    if request.user.is_authenticated:
        return redirect(profile)
    if request.method == "POST":
        form = Signin(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("profile")

            elif request.user.is_superuser:
                messages.error(request, "Invalid credentials")

            else:
                messages.error(request, "Invalid credentials")
                return redirect("signin")
    else:
        form = Signin()
        return render(request, "accounts/login.html", {"form": form})


@login_required(login_url="signin")
def profile(request):
    if  not request.user.is_superuser:
        template = loader.get_template("accounts/profile.html")
        return HttpResponse(template.render({}, request))
    else:
        return redirect("signin")


@login_required(login_url="signin")
def user(request):
    if request.method == "POST":
        form = Userdetail(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return render(request, "thanks.html")
    else:
        form = Userdetail(initial={"username": request.user.username})
    return render(request, "accounts/User details.html", {"form": form})


def signout(request):
    logout(request)
    return redirect(signin)


@login_required(login_url="superuser")
def studentlist(request):
    if request.user.is_superuser:
        mymembers = User_detail.objects.all().values()
        return render(request, "admin/list.html", {"mymembers": mymembers})
    else:
        return redirect("superuser")
    


def superuser(request):
    if request.method == "POST":
        form = Signin(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_superuser:
                auth.login(request, user)
                return redirect("studentlist")
            else:
                messages.error(request, "Invalid credentials")
                return redirect("superuser")
    else:
        form = Signin()
        return render(request, "accounts/superuser.html", {"form": form})
