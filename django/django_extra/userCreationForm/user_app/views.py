from django.shortcuts import render,redirect
# from .forms import CreatUserForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #log user in
            return render(request,'welcome.html',{'form':form})
    else:
        form = UserCreationForm()
        
    return render(request,'index.html',{'form':form})

def register(request):
    pass
