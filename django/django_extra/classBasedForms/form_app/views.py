from django.shortcuts import render,redirect

from .forms import RegistrationForm
# then create an index method:
def index(request):
    form = RegistrationForm() # We will build this class out in just a minute
    context = {
        'myregistrationform': form 
    }
    return render(request, 'formtest/index.html', context)


def register(request):
    if request.method == "POST":
        bound_form = RegistrationForm(request.POST)
    # Now test that bound_form using built-in methods!
    # *************************
    print(bound_form.is_valid())
    
    
    print(bound_form.errors) 
    


def login(request):
    pass
def welcome(request):
    pass