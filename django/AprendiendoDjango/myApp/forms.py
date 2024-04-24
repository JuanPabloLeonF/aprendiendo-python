from django import forms
from django.core import validators

class FormularyArticle(forms.Form):
    title = forms.CharField(
        label='title',
        max_length=40,
        widget=forms.TextInput(attrs={'placeholder': 'title'}),
        required=True,
        validators=[
            validators.MinLengthValidator(4, "Minimo 4 caracteres"),
            validators.RegexValidator('^[A-Za-z ]*$', 'Solo se permiten letras'),
        ]
    )
    content = forms.CharField(label='content', widget=forms.Textarea)
    public = forms.ChoiceField(choices=[(1, "SI"), (0, "No")])
    image = forms.ImageField(label="image")
    