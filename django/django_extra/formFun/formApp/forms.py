from django import forms
# import inbuilt user model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    email = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=100,widget=forms.PasswordInput)


class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(min_length=2, max_length=12)
    last_name=forms.CharField(min_length=2, max_length=12)

    class Meta:
        model=User
        fields=['first_name','last_name','email','password1','password2']