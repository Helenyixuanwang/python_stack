from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            
            first_name = form.cleaned_data.get('first_name')

            # password = form.cleaned_data.get('password1')
            
            request.session['first_name'] = first_name
            
            return redirect('/welcome')
        return render(request,'index.html',{'form':form})
    context = {'form':form}
    return render(request,'index.html', context)

 
    

def welcome(request):
    return render(request, 'welcome.html')

def login_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password= request.POST.get('password1')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            request.session['user_fname'] = user.first_name
            return redirect('/welcome')
        else:
            messages.error(request,"username or email not correct")
            return redirect('/')
    form = CreateUserForm()
    context = {'form':form}
    return render(request,'index.html', context)