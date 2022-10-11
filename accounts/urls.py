from django.urls import path

from . import views

urlpatterns = [
    path("", views.signin, name="signin"),
    path("signin/", views.signin, name="signin"),
    path("superuser/", views.superuser, name="superuser"),
    path("user/", views.user, name="user"),
    path("register/", views.register, name="register"),
    path("signout/", views.signout, name="signout"),
    path("profile/", views.profile, name="profile"),
    path("list/", views.studentlist, name="studentlist"),
]
