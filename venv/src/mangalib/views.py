from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
#  Ne pas oublier d'immporter notre modèle
from .models import Book, Author
#  Importer le module formulaire
from .forms import BookForm
from django.contrib.auth.decorators import login_required, permission_required
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

@permission_required('mangalib.view_book', raise_exception=True) # <app_name>.<action>_<model_name>
def show(request, book_id):
    context = {"book": get_object_or_404(Book, pk = book_id),}
    return render(request, "mangalib/show.html", context)

@permission_required('mangalib.add_book', raise_exception=True) # <app_name>.<action>_<model_name>
def add(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("mangalib:index")
    else:
        form = BookForm()
        
    return render(request, 'mangalib/book-form.html', {"form": form})

@permission_required('mangalib.change_book', raise_exception=True) # <app_name>.<action>_<model_name>
def edit(request, book_id):
    book = Book.objects.get(pk = book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance = book)
        
        if form.is_valid():
            form.save()
            return redirect("mangalib:index")
    else:
        form = BookForm( instance = book)
        
    return render(request, 'mangalib/book-form.html', {"form": form})

@permission_required('mangalib.delete_book', raise_exception=True) # <app_name>.<action>_<model_name>
def remove(request, book_id):
    book = Book.objects.get(pk = book_id)
    book.delete()
    return redirect("mangalib:index")


# Quand on ne peut pas utiliser les décorrateur voici une méthode alternative :
"""
user.has_perm()
    .all()
    .add(<perm1<, ...)
    .remove(<perm2<, ...)
    .clear()
    .set([])
"""

# Méthodes sur  les groiupes

"""
user.groups.set([gr1, gr2])
"""