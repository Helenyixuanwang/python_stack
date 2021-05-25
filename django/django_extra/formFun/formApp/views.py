from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def index(request):
    # myForm=RegisterForm()
    # context={
    #     "myform":myForm
    # }
    login_form = AuthenticationForm()
    context={'myform':login_form}
    return render(request, 'index.html',context)

def register(request):
    print("Inside Register")
    bound_form = RegisterForm(request.POST)
    print(request.POST['first_name'])
    return redirect("/")
    