from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import CreatUserForm
from django.contrib import messages
import random

def index(request):
    form = CreatUserForm() # We will build this class out in just a minute
    context = {
        'form': form, # Form is the variable name referencing the instance of our RegistrationForm class
    }
    return render(request, 'index.html', context)

def register(request):
    if request.method == "POST":
    
        bound_form = CreatUserForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            user = bound_form.cleaned_data.get('username')
            messages.success(request,"Account is successfuly created for " + user)
            return redirect('/success')
        
    else:
        form = CreatUserForm()
        return render(request, 'index.html', {'form':form})

def success(request):

