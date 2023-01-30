from django import forms
from django.forms import ModelForm

from commerce.models import RegisteredUser, SignInUser


class RegisterForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = RegisteredUser
        fields = '__all__'
        labels = {
            'username': 'Name',
            'email': 'Email',
            'phone': 'Phone',
            'password': 'Password',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Phone'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control',}),
        }


class SignInForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = SignInUser
        fields = '__all__'
        labels = {
            'username': 'Name',
            'password': 'Password',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control',}),
        }
