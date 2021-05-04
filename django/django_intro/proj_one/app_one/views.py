#from django.shortcuts import render,HttpResponse

# Create your views here.
#def index(request):
#   return HttpResponse("placeholder to later display a list of all blogs")

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to later display list of blogs")
    
def new(request):
        return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/blogs')

def show(request, number):
    return HttpResponse(f"Placeholder to display blog number {number}.")

def edit(request, number):
    return HttpResponse(f"Placeholder to edit blog {number}.")

def destroy(request, number):
    return redirect('/blogs')
