from django.urls import path

from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("", views.signin, name="signin"),
    path("signin/", views.signin, name="signin"),
    path("superuser/", views.superuser, name="superuser"),
    path("user/", views.user, name="user"),
    path("register/", views.register, name="register"),
    path("signout/", views.signout, name="signout"),
    path("listout/", views.listout, name="listout"),
    path("studentlist/", views.studentlist, name="studentlist"),
    path("<slug:slug>", views.update, name="update"),
    path("update/<str:username>", views.update, name="update"),
    path("update/updaterecord/<str:username>", views.updaterecord, name="updaterecord"),
    path("delete/<str:username>", views.delete, name="delete"),
]
