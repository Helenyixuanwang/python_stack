from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages

from .models import Course, Description, Comment

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request,'index.html', context)

    # return HttpResponse("place holder for home page")

def create(request):
    if request.method=='POST':
        errors = Course.objects.basic_validator(request.POST)
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/')
        new_description = Description.objects.create(desc=request.POST['desc'])
        new_course = Course.objects.create(name=request.POST['name'],description=new_description)
    
        return redirect("/")

def show_delete(request, course_id):
    if request.method == 'GET':
        this_course=Course.objects.get(id=course_id)
        context = {
            'this_course': this_course,
        
        }
        return render(request,'delete.html', context)

    if request.method == 'POST':
        course_to_delete = Course.objects.get(id=course_id)
        print("course ID is ",course_to_delete.id)
        course_to_delete.delete()
        return redirect('/')
    


def comment(request, course_id):
    this_course = Course.objects.get(id = course_id)
    if request.method == 'GET':
        

        context = {
            
            'this_course': this_course,
        }

        return render(request, 'comment.html', context)
    
    if request.method == 'POST':

        comment = Comment.objects.create(comment = request.POST['comment'], course = this_course)
        

        
        return redirect(f'/courses/comment/{course_id}')


