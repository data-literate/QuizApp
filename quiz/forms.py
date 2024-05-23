from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label="User Name", widget=forms.TextInput())
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)
    email = forms.EmailField(help_text='Required.', widget=forms.EmailInput(), label='Email')
