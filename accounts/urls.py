from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("user/", views.user, name="user"),
    # path("signin/", views.signin, name="signin"),
    # path("register/", views.register, name="register"),
    # path('logout', views.logout, name='logout'),
    # path("dashboard/", views.dashboard, name="dashboard"),
]
