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
        return redirect('/success')
    return redirect('/')

def login(request):
    if request.method == 'POST':
        user = User.objects.filter(email = request.POST['email'])
        if user: 
            logged_user = user[0] 
            if bcrypt.checkpw(request.POST['pw'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                
                messages.success(request, "You have successfully logged in!")
                return redirect('/success')
            errors= messages.error(request,"Log in Email or password is not right")
    return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.get(id=request.session['user_id'])
    all_users = User.objects.all()

    context = {
        'this_user':this_user,
        'all_users': all_users,
        

    }

    return render(request, 'success.html',context)

def logout(request):
    
        request.session.flush()
        return redirect('/')
    

        
#Post
def post_message(request):
    if request.method == 'POST':
        this_user = User.objects.get(id=request.session['user_id'])
        this_message = Message.objects.create(message=request.POST['message'], user=this_user)
        print(f'this message id is {this_message.id}, created by {this_user.first_name}')

        return redirect('/success')
    return redirect('/')

def post_comment(request):
    if request.method == 'POST':
        this_user = User.objects.get(id=request.session['user_id'])
        this_message = Message.objects.get(id=request.POST['message_id'])
        this_comment=Comment.objects.create(user=this_user, message=this_message, comment=request.POST['comment'])
        print("this comment is for message ", this_message.id)
        print(f'this comment id is {this_comment.id} to post {this_message.id} by {this_user.first_name}')

        return redirect('/success')
    return redirect('/')