from django.shortcuts import render, redirect

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
        return redirect('/books')
    return redirect('/')

def login(request):
    if request.method == 'POST':
        user = User.objects.filter(email = request.POST['email'])
        if user: 
            logged_user = user[0] 
            if bcrypt.checkpw(request.POST['pw'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                request.session['logged_user']= logged_user.first_name
                
                # messages.success(request, "You have successfully logged in!")
                return redirect('/books')
            errors= messages.error(request,"Log in Email or password is not right")
    return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.get(id=request.session['user_id'])
    
    all_books = Book.objects.all()
    # print(f'there are {all_books.count} books')
    context = {
        'this_user':this_user,
        
        'all_books': all_books,
    }
    return render(request, 'welcome.html',context)

def logout(request):
    
        request.session.flush()
        return redirect('/')

def add_book(request):
    if request.method == 'POST':
        errors = Book.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            print(errors)
            return redirect('/books')
        this_user = User.objects.get(id= request.session['user_id'])
        this_book = Book.objects.create(title=request.POST['title'],desc = request.POST['desc'],uploaded_by = this_user)
        this_book.users_who_like.add(this_user)

        return redirect('/books')
    return redirect('/')

def delete(request, book_id):
    
        print("book id to delete is ", book_id)
        book_to_delete = Book.objects.get(id=book_id)
        book_to_delete.delete()
        return redirect('/books')
    
    
    

def display_book(request, book_id):
    
        this_book = Book.objects.get(id=book_id)
        this_user = User.objects.get(id=request.session['user_id'])

        context = {
            'this_book':this_book,
            'this_user':this_user,
        }
        return render(request, "display_book.html", context)

def update(request, book_id):


    if request.method == 'POST':
        errors = Book.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            print(errors)
            return redirect(f'/books/{book_id}')
        
        book_to_update = Book.objects.get(id=book_id)
        book_to_update.title = request.POST['title']
        book_to_update.desc = request.POST['desc']
        # book_to_update.updated_at = 
        book_to_update.save()
        return redirect(f'/books/{book_id}')

def add_favorite(request,book_id):
    this_book = Book.objects.get(id=book_id)
    this_user = User.objects.get(id= request.session['user_id'])
    this_book.users_who_like.add(this_user)
    return redirect(f'/books/{book_id}')
    
    
def unfavor(request,book_id):
    this_book = Book.objects.get(id=book_id)
    this_user = User.objects.get(id= request.session['user_id'])
    this_book.users_who_like.remove(this_user)
    return redirect(f'/books/{book_id}')
