from django.shortcuts import render,redirect

from .models import User

# Create your views here.
def index(request):
    context = {
        'all_user' : User.objects.all()
    }
    
    return render(request,"index.html", context)

def create(request):
    new_user = User.objects.create(first_name = request.POST['f_name'], 
    last_name=request.POST['l_name'], 
    email_address=request.POST['email'], 
    age= request.POST['age'])
    return redirect('/')

def delete(request):
    if request.method=='POST':
        # print("user_id is ", request.POST['user_id'])
        User.objects.get(id=request.POST['user_id']).delete()
    return redirect('/')

