from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import *


@login_required(login_url="signin")
def index(request):
    return render(request, "index.html", {})


def register(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            password2 = request.POST["password2"]

            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
            )
            user.save()
            login(request, user)
            messages.success(request, "Account Created successfully for " + username)
            return redirect(index)
    else:
        form = Register()
    return render(
        request,
        "accounts/register.html",
        {
            "form": form,
        },
    )


def signin(request):
    if request.user.is_authenticated:
        return redirect(index)
    if request.method == "POST":
        form = Signin(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]

            # try:

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect(index)

            elif user is None:
                messages.error(request, "User does not exist")
                return redirect(signin)
    else:
        form = Signin()
        return render(
            request,
            "accounts/login.html",
            {
                "form": form,
            },
        )


@login_required(login_url="signin")
def user(request):
    if request.method == "POST":
        form = Userdetail(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect(index)
    else:
        form = Userdetail(
            initial={
                "username": request.user.username,
                "email": request.user.email,
            }
        )
    return render(
        request,
        "accounts/User details.html",
        {
            "form": form,
        },
    )


def signout(request):
    logout(request)
    return redirect(signin)


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

            elif user is None:
                messages.error(request, "User does not exist")
                return redirect(superuser)

            elif not user.is_superuser and user is not None:
                messages.error(request, "You are not authorized to view this page")
                return redirect(superuser)

    else:
        form = Signin()
        return render(request, "accounts/superuser.html", {"form": form})


@login_required(login_url="superuser")
def studentlist(request):
    if request.user.is_superuser and request.user.is_authenticated:
        student = User_detail.objects.all().order_by("username").values()
        return render(
            request,
            "admin/list.html",
            {
                "student": student,
            },
        )

    elif not request.user.is_superuser and request.user.is_authenticated:
        messages.error(
            request,
            "You are authenticated as "
            + request.user.username
            + " ,but are not authorized to access this page. Would you like to login to a different account?",
        )
        return redirect(superuser)

    else:
        return redirect(superuser)


def listout(request):
    logout(request)
    return redirect(signin)


@login_required(login_url="signin")
def update(request, username):
    if request.user.is_authenticated and request.user.is_superuser:
        messages.error(request, "Please login with a non administrative account")
        return redirect(signout)
    else:
        form = Updatedetail(
            initial={
                "username": request.user.username,
                "email": request.user.email,
            }
        )
        user = User_detail.objects.get(username=username)
        template = loader.get_template("accounts/update.html")
        return HttpResponse(
            template.render(
                {
                    "user": user,
                    "form": form,
                },
                request,
            )
        )


def delete(request, username):
    student = User_detail.objects.get(username=username)
    student.delete()
    return HttpResponseRedirect(reverse("studentlist"))

def updaterecord(request, username):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    date_of_birth = request.POST['date_of_birth']
    gender = request.POST['gender']
    tel = request.POST['tel']
    user = User_detail.objects.get(username=username)
    user.first_name = first_name
    user.last_name = last_name
    user.date_of_birth = date_of_birth
    user.gender = gender
    user.tel = tel
    user.save()
    return HttpResponseRedirect(reverse(index))