from django.shortcuts import render,redirect,HttpResponse

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
        
        this_show=Show.objects.create(title=request.POST['title'],
                                    network=request.POST['network'],
                                    release_date=request.POST['release_date'],
                                    desc=request.POST['desc'],
                                    )
        print("newly created show id is ", this_show.id)
        id=this_show.id
    
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
    # if request.method=='POST':
        show_to_update=Show.objects.get(id=show_id)
        show_to_update.title=request.POST['title']
        show_to_update.network=request.POST['network']
        show_to_update.release_date=request.POST['release_date']
        show_to_update.desc=request.POST['desc']
        id=show_to_update.id
        show_to_update.save()
        return redirect(f'/shows/{id}')

    

def delete(request,show_id):
    # if request.method=='POST':
        show_to_delete=Show.objects.get(id=show_id)
        show_to_delete.delete()
        return redirect('/shows')
    # return HttpResponse(f'place holder for show {show_id} delete')