from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
#  Ne pas oublier d'immporter notre modèle
from .models import Book, Author
# Create your views here.

#  Les commandes SQL et leur équivalent Django
# SELECT (en SQL) : all() ou get()
# WHERE (en SQL) : filter(), __gt, __lt, __gte, __lte, __startswith
#  ORDER BY (en SQL) : order_by()
#  LIMIT : [:N]
# INSERT INTO : create(), save()
def index (request):
    # je souhaite récupérer tous ce qu'il y a dans la table livre
    context = {
        "books": Book.objects.all()
        }
    
    return render(request, 'mangalib/index.html', context)

def show(request, book_id):
    context = {"book": get_object_or_404(Book, pk = book_id),}
    return render(request, "mangalib/show.html", context)


def add(request):
    author = Author.objects.get(name="Virgil")
    book = Book.objects.create(title = "De Republica", quantity =50 , author = author)
    book.save()
    return redirect("mangalib:index")

def edit (request):
    book = Book.objects.get(title = "Etiam si omnes Ego non !")
    book.title = "Meditationes"
    book.save()
    return redirect("mangalib:index")