from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def index(request):
    return render(request,'form.html')

def process(request):
        
    if request.method == 'POST':
        context = {
            'name': request.POST['name'],
            'lang': request.POST['language'],
            'loc': request.POST['location'],
            'gender': request.POST['gender'],
            'comment': request.POST['comment'],
            
        }
        
    
    # if 'vehicle1' in request.POST:  #both if work for this check.
    if request.POST.get('vehicle1',False):
        context['v1_checked'] = True
        context['check1']='bike'
    else:
        context['v1_checked'] = False
        # return render(request, 'result.html',context)
    
    if request.POST.get('vehicle2', False):
        context['v2_checked']= True
        context['check2']= 'car'
    else:
        context['v2_checked']= False
        # return render(request, 'result.html',context)
    
    if request.POST.get('vehicle3',False):
        context['v3_checked']= True
        context['check3']='boat'
    else:
        context['v3_checked']= False
        # return render(request, 'result.html',context)
    print(context.items())
    return render(request, 'result.html',context)
    
    
    
