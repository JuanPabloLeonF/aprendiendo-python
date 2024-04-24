from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', "first_name", "last_name" , 'password1', 'password2']
        
class  LogingForm(forms.Form):
    username = forms.CharField(
        validators=[
            validators.RegexValidator(regex="^[a-zA-Z0-9]*$", message="El campo solo puede contener letras y numeros", code="invalid_username"),
            validators.MinLengthValidator(4, "El nombre de usuario debe ser mayor o igual a 4 caracteres"),
            validators.MaxLengthValidator(16, "El nombre de usuario debe ser menor o igual a 16 caracteres"),
        ]
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        validators=[
            validators.MaxLengthValidator(16, "La contraseña debe ser menor o igual a 16 caracteres"),
            validators.MinLengthValidator(4, "La contraseña debe ser mayor o igual a 4 caracteres"),
            validators.RegexValidator(regex="^[a-zA-Z0-9]*$", message="La contraseña solo puede contener letras y numeros", code="invalid_password"),
        ]
    )