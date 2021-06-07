# from _typeshed import FileDescriptor
from django.shortcuts import render, redirect, HttpResponse

from .models import *
import bcrypt
from django.contrib import messages


# Create your views here.
def index(request):

    return render(request,'index.html')

def create(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')

        password = request.POST['pw']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(first_name = request.POST['f_name'],
                                    last_name = request.POST['l_name'],
                                    email = request.POST['email'],
                                    password = pw_hash)
        request.session['user_id'] = new_user.id
        request.session['name'] = new_user.first_name
        messages.success(request, "You have successfully registered!")
        return redirect('/dashboard')
    return redirect('/')

def login(request):
    if request.method == 'POST':
        user = User.objects.filter(email = request.POST['email'])
        if user: 
            logged_user = user[0] 
            if bcrypt.checkpw(request.POST['pw'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                request.session['fn'] = logged_user.first_name
                
                # messages.success(request, "You have successfully logged in!")
                return redirect('/dashboard')
            errors= messages.error(request,"Log in Email or password is not right")
        errors= messages.error(request,"Log in Email or password is not right")
    return redirect('/')

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.get(id=request.session['user_id'])
    
    

    context = {
        'this_user':this_user,
        'liked_hobbies': this_user.liked_hobbies.all(),
        # all hobbies created by current user
        'all_hobbies': Hobby.objects.filter(creator = this_user),
        'liked_hobbies': Hobby.objects.filter(like = this_user).exclude(creator = this_user),
        # all hobbies created by buddies
        'others_hobbies': Hobby.objects.exclude(creator= this_user).exclude(like= this_user),
    
    }

    return render(request, 'dashboard.html',context)

def logout(request):
    
        request.session.flush()
        return redirect('/')

def new(request):
    if 'user_id' not in request.session:
        return redirect("/")
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        "all_hobbies": Hobby.objects.all(),
    }
    return render(request,"newhobby.html",context)

def create_hobby(request):
    if request.method == 'POST':
        this_user = User.objects.get(id=request.session['user_id'])
        errors= Hobby.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/hobbies/new')
        new_hobby = Hobby.objects.create(name=request.POST['name'],
                                        description = request.POST['description'],
                                        creator = this_user)

        this_user.liked_hobbies.add(new_hobby)
        messages.success(request,"You have created a new hobby")
        return redirect('/dashboard')

def delete_hobby(request, hobby_id):
    if 'user_id' not in request.session:
        return redirect("/")
    hobby_to_delete = Hobby.objects.get(id=hobby_id)
    hobby_to_delete.delete()
    return redirect('/dashboard')  

def edit_hobby(request, hobby_id):
    if 'user_id' not in request.session:
        return redirect("/")
    this_hobby = Hobby.objects.get(id=hobby_id)
    this_user = User.objects.get(id=request.session['user_id'])
    
    
    context = {
        'this_hobby':this_hobby,
        'this_user': this_user,
    }
    return render(request,'edit_hobby.html',context)


def update_hobby(request, hobby_id):
    if request.method == 'POST':
        errors= Hobby.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/hobbies/{hobby_id}/edit')
        else:
            hobby_to_update = Hobby.objects.get(id=hobby_id)
            hobby_to_update.name = request.POST['name']
        
            hobby_to_update.description = request.POST['description']
            hobby_to_update.save()
            return redirect('/dashboard')
    return redirect('/dashboard')

def display_hobby(request, hobby_id):
    this_user = User.objects.get(id=request.session['user_id'])
    this_hobby = Hobby.objects.get(id=hobby_id)
    hobby_creator = this_hobby.creator
    context = {
        'this_hobby':this_hobby,
        'this_user':this_user,
        
        
        
    }
    return render(request,'display_hobby.html',context)

def display_buddie(request,user_id):
    this_user = User.objects.get(id = user_id)

    context = {
        'this_user': this_user,
    }
    return render(request,'display_buddie.html',context)

def like(request, hobby_id):
    this_hobby = Hobby.objects.get(id=hobby_id)
    this_user = User.objects.get(id=request.session['user_id'])
    this_user.liked_hobbies.add(this_hobby)
    return redirect('/dashboard')

def dislike(request, hobby_id):
    this_hobby = Hobby.objects.get(id=hobby_id)
    this_user = User.objects.get(id=request.session['user_id'])
    this_user.liked_hobbies.remove(this_hobby)
    return redirect('/dashboard')


