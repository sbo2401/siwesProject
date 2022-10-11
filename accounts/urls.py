from django.urls import path

from . import views

urlpatterns = [
    path("", views.signin),
    path("user/", views.user, name="user"),
    path("register/", views.register, name="register"),
    path('signout/', views.signout, name='signout'),
    path("profile/", views.profile, name="profile"),
]
