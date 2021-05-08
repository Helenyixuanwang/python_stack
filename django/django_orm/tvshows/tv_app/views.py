from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .models import Show

# Create your views here.
def allshow(request):
    context = {
        'all_show': Show.objects.all()
    }
    
    return render(request, 'index.html',context)

def newshow(request):
    return render(request,'add_newshow.html')

def create(request):
    if request.method=='POST':
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/shows/new')
        
        this_show=Show.objects.create(title = request.POST['title'],
                                        network = request.POST['network'],
                                        release_date = request.POST['release_date'],
                                        desc = request.POST['desc'],
                                        )
        print("newly created show id is ", this_show.id)
        id=this_show.id
        messages.success(request, "Show successfully created")
        return redirect(f'/shows/{id}')
    

    
def show_display(request, show_id):
    current_show =Show.objects.get(id=show_id)
    context = {
        'this_show': current_show,
    }
    return render(request,'newshow_display.html', context)


def edit(request,show_id):
    # if  request.method=='POST':<!-- for this assignment, routings matter,I did not use this method to check if it is valid-->
            current_show=Show.objects.get(id=show_id)
            context = {
                'show': current_show
            }
            return render(request,'edit_show.html', context)
    
        

def update(request,show_id):
    if request.method=='POST':
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect(f'/shows/{show_id}/edit')
        else:
        
            show_to_update=Show.objects.get(id=show_id)
            show_to_update.title=request.POST['title']
            show_to_update.network=request.POST['network']
            show_to_update.release_date=request.POST['release_date']
            show_to_update.desc=request.POST['desc']
            # id=show_to_update.id
            show_to_update.save()
            messages.success(request, "show successfully updated")
            return redirect(f'/shows/{show_id}')

    

def delete(request,show_id):
    if request.method=='POST':
        show_to_delete=Show.objects.get(id=request.POST['item_to_delete'])
        show_to_delete.delete()
        return redirect('/shows')
    else:
        return redirect('/')
    # return HttpResponse(f'place holder for show {show_id} delete')