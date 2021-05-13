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
        'title':this_book.title,
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
        book_id = this_book.id
    print(request.POST)
    return redirect(f'/books/{book_id}')

def add_book_to_author(request,author_id):
        if request.method == 'POST':
            print(request.POST['book_id'])
            this_author=Author.objects.get(id=author_id)
            this_book = Book.objects.get(id=request.POST['book_id'])
            this_author.books.add(this_book)
            author_id = this_author.id
        print(request.POST)
        return redirect(f'/authors/{author_id}')

def authors(request):
    context = {
        'all_authors': Author.objects.all(),
        
    }
    return render(request, "authors.html", context)

def show_author(request, author_id):
    this_author = Author.objects.get(id=author_id)
    context = {
        'author_id': this_author.id,
        'f_name': this_author.first_name,
        'l_name': this_author.last_name,
        'notes' : this_author.notes,
        'authors': Author.objects.all(),
        'all_books':Book.objects.all(),
        'books': this_author.books.all(),
        
    }
    return render(request, 'showauthor.html', context)

def add_author(request):
    if request.method == 'POST':
        new_author=Author.objects.create(first_name=request.POST['f_name'],
                                        last_name=request.POST['l_name'],
                                        notes= request.POST['notes'])
    return redirect('/authors')
    

    

