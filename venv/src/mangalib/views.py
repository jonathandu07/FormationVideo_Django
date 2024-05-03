from django.shortcuts import render
from django.http import HttpResponse
#  Ne pas oublier d'immporter notre modèle
from .models import Book
# Create your views here.
def index (request):
    # je souhaite récupérer tous ce qu'il y a dans la table livre
    context = {"books": Book.objects.all()}
    
    return render(request, 'mangalib/index.html', context)