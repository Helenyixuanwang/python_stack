from django.shortcuts import render,redirect

from .models  import Ninja, Dojo


# Create your views here.
def index(request):
    context = {
        'all_ninja': Ninja.objects.all(),
        'all_dojo': Dojo.objects.all(),
    }
    return render(request, "index.html", context)


def create_dojo(request):
    if request.method == 'POST'and request.POST['name']:
        new_dojo = Dojo.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])
    return redirect('/')

def create_ninja(request):
    if request.method == 'POST'and request.POST['f_name'] and request.POST['l_name']:
        new_ninja = Ninja.objects.create(first_name=request.POST['f_name'], 
        last_name=request.POST['l_name'], 
        dojo_id =request.POST['dojo'])
    return redirect('/')

def delete_dojo(request):
    if request.method == 'POST':
        
        print("dojo_id is ", request.POST['dojo_id_todelete'])
        Dojo.objects.get(id=request.POST['dojo_id_todelete']).delete()
    return redirect('/')