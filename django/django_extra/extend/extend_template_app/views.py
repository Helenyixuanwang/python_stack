from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'base.html')

def about(request):
    return render(request,'about.html')

def home(request):
    return render(request, "home.html")

def contact(request):
    return render(request, 'contact.html')