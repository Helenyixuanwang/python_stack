from django.shortcuts import render,redirect

from .models  import Book, Author


# Create your views here.
def index(request):
    context = {
        'all_books': Book.objects.all(),
        
    }
    return render(request, "index.html", context)

def add_book(request):
    if request.method == 'POST':
        new_book=Book.objects.create(title=request.POST['title'],
                                        desc= request.POST['desc'])
    return redirect('/')

def show_book(request,book_id):
    this_book=Book.objects.get(id=book_id)
    context = {
        'book_id': this_book.id,
        'desc': this_book.desc,
        'authors': this_book.authors.all(),
        'all_authors': Author.objects.all(),
        
    }
    return render(request, 'showbook.html', context)

def add_author_to_book(request,book_id):
    if request.method == 'POST':
        print(request.POST['author_id'])
        this_book=Book.objects.get(id=book_id)
        this_author = Author.objects.get(id=request.POST['author_id'])
        this_book.authors.add(this_author)
    print(request.POST)
    return redirect(f'/books/{book_id}')


    

