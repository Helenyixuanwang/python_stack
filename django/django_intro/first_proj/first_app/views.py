#from django.shortcuts import render
#from django.shortcuts import render, HttpResponse
#def index(request):
 #  return HttpResponse("This is my response!")

# Create your views here.
from django.shortcuts import render
    
def index(request):
    context = {
    	"name": "Noelle",
    	"favorite_color": "turquoise",
    	"pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)
