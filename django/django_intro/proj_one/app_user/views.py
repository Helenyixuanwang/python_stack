
from django.shortcuts import render, HttpResponse, redirect

def create_user(request):
    return HttpResponse("placeholder for users to create a new user record")

def login(request):
    return HttpResponse("placeholder for users to log in")

def display(request):
    return HttpResponse("placeholder to later display all the list of users")