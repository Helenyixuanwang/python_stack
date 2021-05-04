from django.shortcuts import render,redirect, HttpResponse
import random
from datetime import datetime

def index(request):
    if not 'gold'  in request.session or not 'activities' in request.session:
        request.session['gold']= 0
        request.session['activities'] = []
    return render(request, 'index.html')

def reset(request):
    request.session.flush()
    return redirect('/')

def get_gold_farm(request):
    time_stamp = datetime.now().strftime("%m/%d/%Y %I:%M%p")
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        if request.POST['location']=='farm':
            current_gold = random.randint(10,20)
            request.session['gold'] += current_gold
            request.session['activities'].append("earn " +str(current_gold)+" gold at farm " +time_stamp)
        elif request.POST['location']== 'cave':
            current_gold = random.randint(5,10)
            request.session['gold'] += current_gold
            request.session['activities'].append("earn " +str(current_gold)+" gold at cave " +time_stamp)
        elif request.POST['location'] == 'house':
            current_gold = random.randint(2,5)
            request.session['gold'] += current_gold
            request.session['activities'].append("earn " +str(current_gold)+" gold at house " +time_stamp)
        elif request.POST['location'] =='casino':
            current_gold = random.randint(-50,50)
            request.session['gold'] += current_gold
            if current_gold >=0:
                request.session['activities'].append("earn " +str(current_gold)+" gold at casino " +time_stamp)
            else:
                request.session['activities'].append("lose " +str(abs(current_gold))+" gold at casino,so sad " +time_stamp)

    
    return redirect('/')

