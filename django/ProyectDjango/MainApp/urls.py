from django.urls import path
from MainApp import views

urlpatterns = [
    path("", views.index, name="index"),
    path("404/", views.pageNotFound , name="404"),
    path("registerPage/", views.registerPage, name="registerPage"),
    path("logingPage/", views.logingPage, name="logingPage"),
    path("logoutPage/", views.logoutPage, name="logoutPage"),
]