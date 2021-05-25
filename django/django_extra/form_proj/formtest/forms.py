from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class RegistrationForm(forms.Form):
#     first_name = forms.CharField(max_length=45)
#     last_name = forms.CharField(max_length=45)
#     email = forms.EmailField()
#     password = forms.CharField(max_length=100, widget=forms.PasswordInput)
#     confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)




class CreatUserForm(UserCreationForm):
    

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'password': forms.PasswordInput(),
        }