from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from MainApp import forms

def index(request):
    context = {
        "title": "Inicio"
    }
    return render(request, "MainApp/index.html", context)

def pageNotFound(request, exception):
    return render(request, "layouts/404.html", status=404)

def registerPage(request):
    
    formRegister = forms.RegisterForm()
    if (request.method == "POST"):
        formRegister = forms.RegisterForm(request.POST)
        if (formRegister.is_valid()):
            formRegister.save()
            messages.success(request, f"el usuario: {formRegister.cleaned_data.get('username')} fue Registrado con exito")
            return redirect("index")
    
    
    context = {
        "title": "Registrarse",
        "formRegister": formRegister
    }
    return render(request, "user/registerPage.html", context)

def logingPage(request):
    
    logingForm = forms.LogingForm()
    if (request.method == "POST"):
        logingForm = forms.LogingForm(request.POST)
        if (logingForm.is_valid()):
            userName = logingForm.cleaned_data.get('username')
            password = logingForm.cleaned_data.get('password')
            user = authenticate(request, username=userName, password=password)
            if user is not None:
                messages.success(request, f"Bienvenido {logingForm.cleaned_data.get('username')}")
                login(request, user)
                return redirect("index")   
            else:
                messages.error(request, "Credenciales invalidas")
    
    context = {
        "title": "Iniciar Sesion",
        "formLoging": logingForm
    }
    return render(request, "user/logingPage.html", context)

def logoutPage(request):
    logout(request)
    messages.success(request, "Sesion Cerrada con exito")
    return redirect("index")