from django.shortcuts import render,redirect

from .models import User

# Create your views here.

def index(request):

    context = {
        "all_the_users" : User.objects.all()
    }
    print(context.items())
    return render(request, "index.html", context)

def process(request):
    if request.method == 'POST':
        new_user = User.objects.create(first_name = request.POST['f_name'], last_name=request.POST['l_name'],email_address=request.POST['email'], age= request.POST['age'])
    return redirect('/')


