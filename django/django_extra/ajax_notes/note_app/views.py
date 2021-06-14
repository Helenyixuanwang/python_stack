from django.shortcuts import render,redirect

from .models import Note

# Create your views here.
def index(request):
    all_notes = Note.objects.all()
    context = {
        'all_notes': all_notes,
    }
    return render(request, 'index.html', context)

def create_note(request):
    if request.method == 'POST':
        new_note= Note.objects.create(title = request.POST['title'],
                                        desc = request.POST['desc'])
        return redirect('/')
    return redirect('/')

def create_ajax(request):
    all_notes = Note.objects.all()
    if request.method == 'POST':
        note= Note.objects.create(title = request.POST['title'],
                                        desc = request.POST['desc'])
        context = {
            'note': note,
            'all_notes':all_notes,
        }
        return render(request, 'index.html',context)
    
    

def edit_note(request, note_id):
    this_note = Note.objects.get(id = note_id)
    context = {
        'this_note': this_note,

    }
    return render(request, 'index.html', context)

def delete(request):

    if request.method == 'POST':
        note_to_delete = Note.objects.get(id = request.POST['note_to_delete'])
        note_to_delete.delete()
        return redirect('/')
    return redirect('/')

def delete_ajax(request):
    all_notes = Note.objects.all()
    if request.method == 'POST':
        note_to_delete = Note.objects.get(id = request.POST['note_to_delete'])
        note_to_delete.delete()
        context = {
        'all_notes': all_notes,
    }
    return render(request, 'index.html', context)


def update(request,note_id):
    
    if request.method == 'POST':
        note_to_update = Note.objects.get(id=note_id)
        note_to_update.desc = request.POST['desc']
        note_to_update.save()
    
        return redirect('/')

# def display(request):
#     all_notes = Note.objects.all()
#     context = {
#         'all_notes': all_notes,
#     }
#     return render(request,'display.html',context)