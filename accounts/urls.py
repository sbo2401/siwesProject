from django.urls import path

from . import views

urlpatterns = [
    path("", views.signin, name="signin"),
    path("signin/", views.signin, name="signin"),
    path("superuser/", views.superuser, name="superuser"),
    path("user/", views.user, name="user"),
    path("register/", views.register, name="register"),
    path("signout/", views.signout, name="signout"),
    path("listout/", views.listout, name="listout"),
    path("profile/", views.profile, name="profile"),
    path("studentlist/", views.studentlist, name="studentlist"),
    path("delete/<str:username>", views.delete, name="delete"),
    path("update/<str:username>", views.update, name="update"),
]
