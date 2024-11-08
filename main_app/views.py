from django.shortcuts import render
from .models import Cat

# Import HttpResponse to send text-based responses


# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'about.html')


def cat_index(request):
    cats = Cat.objects.all()
    # Render the cats/index.html template with the cats data
    return render(request, 'cats/index.html', {'cats': cats})