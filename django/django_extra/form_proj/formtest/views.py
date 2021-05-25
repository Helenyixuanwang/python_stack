from django.shortcuts import render,redirect

from .forms import CreatUserForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# from .forms import RegistrationForm
# then create an index method:
def index(request):
    form = CreatUserForm() # We will build this class out in just a minute
    context = {
        'form': form, # Form is the variable name referencing the instance of our RegistrationForm class
    }
    return render(request, 'index.html', context)

# Inside your app's views.py file
# This is the method that is running in response to that form submission
def register(request):
    
    if request.method == "POST":
    
        bound_form = CreatUserForm(request.POST)
    # Now test that bound_form using built-in methods!
    # *************************
        # print(bound_form.is_valid()) 
        if bound_form.is_valid():
            bound_form.save()
            user = bound_form.cleaned_data.get('username')
            messages.success(request,"Account is successfuly created for " + user)
            return redirect('/')
        
    else:
        form = CreatUserForm()
        return render(request, 'index.html', {'form':form})
    

def welcome(request):
    all_users = User.objects.all()
    context = {
        'all_users': all_users,
    }
    return render(request, 'welcome.html',context)
def login_page(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request,username=username, password = password)
        if user is not None:
            login(request, user)
            redirect('/welcome')
        else:
            messages.error(request,"username or password incorrect")
            return render(request,'index.html',)


