from django.shortcuts import render,redirect
# from .forms import CreatUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            password2= form.cleaned_data.get('password2')
            if password!='' and password2!='':
                request.session['new'] = True
                request.session['username'] = username
            
            return redirect('/welcome')
        return render(request,'index.html',{'form':form})
    context = {'form':form}
    return render(request,'index.html', context)

 
    

def welcome(request):
    return render(request, 'welcome.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password= request.POST.get('password1')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            request.session['username'] = username
            return redirect('/welcome')
        else:
            messages.error(request,"username or email not correct")
            return redirect('/')
    form = UserCreationForm()
    context = {'form':form}
    return render(request,'index.html', context)

def logout_user(request):
    logout(request)
    return redirect('/')