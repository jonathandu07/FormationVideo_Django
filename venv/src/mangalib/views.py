from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
#  Ne pas oublier d'immporter notre modèle
from .models import Book
# Create your views here.

#  Les commandes SQL et leur équivalent Django
# SELECT (en SQL) : all() ou get()
# WHERE (en SQL) : filter()
#  ORDER BY (en SQL) : order_by()
#  LIMIT : [:N]
def index (request):
    # je souhaite récupérer tous ce qu'il y a dans la table livre
    context = {
        "books": Book.objects.all().filter(author_id = 2)
        }
    
    return render(request, 'mangalib/index.html', context)

def show(request, book_id):
    context = {"book": get_object_or_404(Book, pk = book_id),}
    return render(request, "mangalib/show.html", context)