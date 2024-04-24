from django.urls import path
from Pages import views

urlpatterns = [
    path("pages/<str:slug>/", views.page, name="page"),
]
