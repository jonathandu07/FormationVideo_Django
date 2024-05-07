# FormationVideo_Django

## Commandes initiales :

1. **Je fais un environnemnt virtuel :**
   `python -m venv venv`

2. **Je me déplace dans l'environnement virtuel que je vient de créer :**
   `cd venv`

3. **J'active l'environnement virtuel :**
   `.\Scripts\Activate`

4. **Je met à jour les paquets pip :**
   `python.exe -m pip install --upgrade pip`

5. **J'installe la dernière version de django :**
   `python -m pip install Django`

6. **Je sauvegarde ma configuration :**
   `pip freeze > requierements.txt`

---

## Création et gestion du projet

7. **Je créais mon projet :**
   `django-admin startproject main`

- le projet se nomme "main" car à l'intérieur de ce dossier je vais avoir les fichiers principaux

8. **Je ronomme le dossier main :**

- Je le renomme en "src" pour ne pas avoir de confusion avec le dossier main à l'intérieur.

9. **Je me déplace dans le répertoire `src` :**
   `cd src`

10. **Je lance le serveur :**
    `python manage.py runserver`

11. bis **pour retirer l'érreur suivante :**

```cli
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
```

Faire le commande suivante dans le dossier **src** :
`python manage.py migrate`

- Permet de faire la migration de la base de donnée en sqlite.

11. **Je créais ma première application :**
    `python manage.py startapp mangalib`

- Ici l'application s'appelle `mangalib`

---

## gestion des apps

12. **Je créais un fichier `urls.py` dans le dossier `mangalib`**

13. **Je défini la route pour une page de l'app `mangalib` :**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

14. **Je créais ma première vue dans le fichier `urls.py` :**

```python
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index (request):
    return HttpResponse ("Bienvenue")
```

- Je fais références au fichier `urls.py` dans l'application `mangalib`.

15. **Je créais ma route dans le fichier `urls.py` du dossier `main` :**

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('manga/', include('mangalib.urls'))
]
```

16. **J'ajoute l'app dans le fichier `settings.py` :**

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Mes applications
    'mangalib'
]
```

17. **Je créais un répertoire `templates` dans l'app `mangalib` :**

- Puis je créais un sous dossier nommé du nom de mon application.

18. **Dans le fichier `views.py` qui se trouve dans l'application mangalib, j'aoute cela :**

- Dans un premier temps le module chargeur de template en ajoutant la ligne suivante : `from django.template import loader`
- Je créais une varitable de template nomée `context`.

```python
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index (request):
    context = {"message": "Hello, world! !"}
    template = loader.get_template("mangalib/index.html")
    return HttpResponse(template.render(context, request))
```

- Ajout de la varibale de template dans le fichier html.

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Mes mangas</title>
  </head>
  <body>
    <h1>Bienvenue sur Mangalib !</h1>
    <p>{{message}}</p>
  </body>
</html>
```

19. **Ajout des fichiers statics**

```html
{% load static %}
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Mes mangas</title>
    <link rel="stylesheet" href="{% static 'mangalib/css/main.css' %}" />
  </head>
  <body>
    <h1>Bienvenue sur Mangalib !</h1>
    <p>{{message}}</p>
  </body>
</html>
```

- à la racine de chaque application, comme pour templates, créer un fichier static qui sert pour le css, le scss ou le JS.

20. **Création d'un fichier stactic global :**

- Créer un fichier stactic dans l'application du projet, c'est à dire `main`.
- Aller dans le fichier `settings.py` et j'immorte le module **OS** et j'ajoute **STATICFILES_DIRS** comme suit :

```python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
#  J'aoute d'autres chemins pour les fichiers statics
STATICFILES_DIRS = [
    os.path.join('main/static')
]
```

---

## Balises et filtres

**La balise `comment` :**

- Cette balise sert à ne pas afficher sur la page ce qu'il y a entere les balises.

```html
{% comment %}
<p>Voici du code qui sera ignoré grâce à la balise "comment"</p>
{% endcomment %}
```

**La balise `Lorem` :**

- Permet de générer du text Lorem ipsum.

```html
{% lorem 250 w %}
```

ici il y a 250 mot (w) qui seront générés.

```html
{% lorem 250 p random %}
```

- Ci-dessus il est possible de voir que je peux utiliser la lettre `p` pour demander un paragraphe et également `random` pour utiliser une fonction aléatoire.

**La balise `debug` :**

```html
<h2>Voici la balise Debug</h2>
{% debug %}
```

**La balise `date` :**

- La balise date à un formatage complexe donc se fier à la documentation

```html
<h2>La balise date</h2>
{% now 'd m y H:i:s' %}
```

**La balise `Include` :**

- Ne pas oublier le `./`

```html
<h2>Importation d'un fichier html extérieur</h2>
{% include "./import.html" %}
```

**La balise `url` :**

- Voici comment faire du routage.

```html
    <button>
        <a href="{% url  'indexMangalib' %}">
            <p>Découvir la page manga </p>
        </a>
    </button>
</body>
```

**La balise `if` :**

```html
<h2>Les balises condtionelles</h2>
{% if numberNews > 0 %}
<p>Des news sont disponibles !</p>
{% else %} {{numberNews}} {% endif %}
```

**La balise `for` :**

```html
<h2>Les boucles</h2>
{% for u in UserList %}
<p>{{u}}</p>
{% empty %}
<p>Pas d'utilisateurs...</p>
{% endfor %}
```

### Création de balises et de filtres

**Récupérer le premier caractère d'une chaines de carractères**

```python
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def first_char(value):
    return value[0]
```

- Créer un dossier dans l'application et le nommer `templatetags`.
- Modifier le fichier html comme suit :

```html
{% load static %} {% load customtags %}
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Mes mangas</title>
    <link rel="stylesheet" href="{% static 'mangalib/css/main.css' %}" />
    <link rel="stylesheet" href="{% static '/css/global.css' %}" />
  </head>

  <body>
    <h2>Filtre personnalisé</h2>
    <p>{{message | first_char }}</p>
  </body>
</html>
```

- `{% load customtags %}` est primordial pour charger son fichier python.
  Il est possible également de renommer les fonctions avec les décorrateurs :

````python
@register.filter(name = "longueur_de_ça")
def checkstrlen(value, size):
    return len(value) == size
    ```
````

- Voici le html :

```html
{% load static %} {% load customtags %}
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Mes mangas</title>
    <link rel="stylesheet" href="{% static 'mangalib/css/main.css' %}" />
    <link rel="stylesheet" href="{% static '/css/global.css' %}" />
  </head>

  <body>
    <h2>Filtre compteur de carractères</h2>
    <p>{{message | longueur_de_ça:5 }}</p>
  </body>
</html>
```

**Balise personnalisé :**

```python
from django import template

register = template.Library()

@register.simple_tag
def hello_world():
    return "Hello, world!"

```

- Le coter HTML

```html
{% load static %} {% load customtags %} {% load customBalises %}
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Mes mangas</title>
    <link rel="stylesheet" href="{% static 'mangalib/css/main.css' %}" />
    <link rel="stylesheet" href="{% static '/css/global.css' %}" />
  </head>

  <body>
    <h2>Balise personnalisée</h2>
    <p>{% hello_world %}</p>
  </body>
</html>
```

---

## Les modèles

Gestion de bases de données.

```python
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=64, unique = True)


class Book(models.Model):
    title = models.CharField(max_length=32, unique = True)
    quantity = models.IntegerField(default=1)
    # Première relation
    author = models.ForeignKey(Author, on_delete=DO_NOTHING)

```

- Je suis allé dans le fichier `models.py` et je l'ai rempli avec ce qu'il y a ci-dessus.
  Pour faire une migration : `python manage.py makemigrations mangalib`
  **résultat dans l'invité de commande :**

```powershell
PS D:\alpha\Documents\Programation\Django\FormationVideo_Django\FormationVideo_Django\venv\src> python manage.py makemigrations mangalib
Migrations for 'mangalib':
  mangalib\migrations\0001_initial.py
    - Create model Author
    - Create model Book
PS D:\alpha\Documents\Programation\Django\FormationVideo_Django\FormationVideo_Django\venv\src>
```

Pour d'autre application remplacer `managlib` par le nom de l'application en question.

**Pour vérifier les requètes :**
`python manage.py sqlmigrate mangalib 0001`
Le **0001** représente le numéro de la migration.

```powershell
PS D:\alpha\Documents\Programation\Django\FormationVideo_Django\FormationVideo_Django\venv\src> python manage.py sqlmigrate mangalib 0001
BEGIN;
--
-- Create model Author
--
CREATE TABLE "mangalib_author" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(64) NOT NULL UNIQUE);
--
-- Create model Book
--
CREATE TABLE "mangalib_book" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(32) NOT NULL UNIQUE, "quantity" integer NOT NULL, "author_id" bigint NOT NULL REFERENCES "mangalib_author" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "mangalib_book_author_id_bc892452" ON "mangalib_book" ("author_id");
COMMIT;
PS D:\alpha\Documents\Programation\Django\FormationVideo_Django\FormationVideo_Django\venv\src>
```

le dossier `migrations` vient d'apparaitre dans le dossier de l'application.

**Pour effectuer la migration :**
`python manage.py migrate`

```powershell
PS D:\alpha\Documents\Programation\Django\FormationVideo_Django\FormationVideo_Django\venv\src> python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, mangalib, sessions
Running migrations:
  Applying mangalib.0001_initial... OK
```

**Pour afficher les éléments d'une table :**

- Dans le fichier `views.py` :

```python
from django.shortcuts import render
from django.http import HttpResponse
#  Ne pas oublier d'immporter notre modèle
from .models import Book
# Create your views here.
def index (request):
    # je souhaite récupérer tous ce qu'il y a dans la table livre
    context = {"books": Book.objects.all()}

    return render(request, 'mangalib/index.html', context)
```

1. Importer le module `.models`
2. faire une variable et lui attribuer tous les éléments d'une table.
3. Renvoyer ses éléments en faisant comme suit :

```html
{% load static %} {% load customtags %} {% load customBalises %}
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Mes mangas</title>
    <link rel="stylesheet" href="{% static 'mangalib/css/main.css' %}" />
    <link rel="stylesheet" href="{% static '/css/global.css' %}" />
  </head>

  <body>
    <h2>Liste des livre</h2>
    <ul>
      {% for book in books %}
      <li>{{book.title}}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

4. Création d'une page par article :

```python
from django.urls import path
from . import views

# Je crréais une variable pour mon app
app_name = "mangalib"
urlpatterns = [
    # Show est la méthode qui est dans views.py
    path("<int:book_id>/", views.show, name="show"), # manga/<id>
]
```

- Dans le fichier **urls.py**

5. Modifier le fichier **views.py** :

```python
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
#  Ne pas oublier d'immporter notre modèle
from .models import Book
# Create your views here.
def show(request, book_id):
    context = {"book": get_object_or_404(Book, pk = book_id)}
    return render(request, "mangalib/show.html", context)
```

- Je créais une méthode **show** qui renvoie tout les éléments d'un objets livre sur la page **show**.

6. Je créais un template pour la page **show**

```html
{% load static %}
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{{book.title}}</title>
    <link rel="stylesheet" href="{% static 'mangalib/css/main.css' %}" />
    <link rel="stylesheet" href="{% static '/css/global.css' %}" />
  </head>
  <body>
    <h1>{{book.title}}</h1>
    <p>Quantité : {{book.quantity}}</p>
    <p>Auteur : {{book.author.name}}</p>
    <p>Id du livre : {{book.id}}</p>
    <p>
      <a href="{% url 'mangalib:index' %}"
        >&laquo; Revenir à la liste des livres</a
      >
    </p>
  </body>
</html>
```

---

## Les gestionnaires

- **SELECT \* FROM mangalib_book;** -> en django `"books": Book.objects.all()`
  il est aussi possible d'utiliser la méthode `get()` -> `book = Book.objects.get(title="Nom du Livre")`

- **SELECT \* FROM mangalib_book ORDER BY title;** -> en django `"books": Book.objects.all().order_by("title")`
  Classe les titres par ordre alphabétique par défaut.

- **SELECT \* FROM mangalib_book ORDER BY title DESC;** -> en django `"books": Book.objects.all().order_by("-title")`
  Classe les titres par ordre non alphabétique (décroissant).

- **SELECT \* FROM mangalib_book LIMIT 5;** -> en django `"books": Book.objects.all()[:5]`
  Permet de récupéer les 5 premiers éléments d'une liste.

- **SELECT \* FROM mangalib_book WHERE author_id = 2;** -> en django `"books": Book.objects.all().filter(author_id = 2)`
  Permet de récupéer les livres dont l'id de l'auteur est 2, il s'agit de Virgile.

- **SELECT \* FROM mangalib_book WHERE quantity > 100;** -> en django `"books": Book.objects.all().filter(quantity__gt = 100)`
  Permet de récupéer les livres dont la quantité est supérieure à 100. `__gt` signifie : **greater than**

- **`SELECT * FROM mangalib_book WHERE quantity < 100;`** -> en django `"books": Book.objects.all().filter(quantity__lt = 100)`
  Permet de récupéer les livres dont la quantité est inférieur à 100. `__lt` signifie : **less than**

- **SELECT \* FROM mangalib_book WHERE quantity >= 100;** -> en django `"books": Book.objects.all().filter(quantity__gte = 100)`
  Permet de récupéer les livres dont la quantité est supérieure ou égale à 100. `__gte` signifie : **greater than or equal to**

- **`SELECT * FROM mangalib_book WHERE quantity <= 100;`** -> en django `"books": Book.objects.all().filter(quantity__lte = 100)`
  Permet de récupéer les livres dont la quantité est inférieur ou égale à 100. `__lte` signifie : **less than or equal to**

- **SELECT \* FROM mangalib_book WHERE title LIKE 'Éthique à Nicomaque%';** -> en django `"books": Book.objects.all().filter(title__startswith = "Éthique à Nicomaque")`
  Permet de récupéer les livres dont le titre commence par : **Éthique à Nicomaque**. `__startswith` signifie : **starts with**

### La commande INSERT

```python
def add(request):
    author = Author.objects.get(name="Virgil")
    book = Book.objects.create(title = "De Republica", quantity =50 , author = author)
    book.save()
    return redirect("mangalib:index")
```

- Comment ajouter un élément en base de donnée mais sans utiliser de formulaire

- **Modifier :**

```python
def edit (request):
    book = Book.objects.get(title = "Etiam si omnes Ego non !")
    book.title = "Meditationes"
    book.save()
    return redirect("mangalib:index")
```

- **Supprimer :**

```python
def remove(request):
    book = Book.objects.get(title = "Ce que tu veux")
    book.delete()
    return redirect("mangalib:index")
```

**Il est nécessaire de créer des chemins dans le fichiers views**

```python
from django.urls import path
from . import views

# Je crréais une variable pour mon app
app_name = "mangalib"
urlpatterns = [
    path('', views.index, name='index'), # manga/
    # Show est la méthode qui est dans views.py
    path("<int:book_id>/", views.show, name="show"), # manga/<id>
    path('ajouter-livre/', views.add, name="add"),
    path('modifier-livre/', views.edit, name="edit"),
    path('supprimer-livre/', views.remove, name="delete"),
]
```

**Il faut aussi créer les liens dans le template**

```html
{% load static %} {% load customtags %} {% load customBalises %}
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Mes mangas</title>
    <link rel="stylesheet" href="{% static 'mangalib/css/main.css' %}" />
    <link rel="stylesheet" href="{% static '/css/global.css' %}" />
  </head>

  <body>
    <p><a href="{% url 'mangalib:add' %}">ajouter un livre</a></p>
    <p><a href="{% url 'mangalib:edit' %}">modifier un livre</a></p>
    <p><a href="{% url 'mangalib:delete' %}">supprimer un livre</a></p>
  </body>
</html>
```

---

## Administration

1. Créer un super utilisateur : `python manage.py createsuperuser``

```cli
 python manage.py createsuperuser
Nom d’utilisateur (leave blank to use 'alpha'): jonathan
Adresse électronique: jonathan.admin@nac.fr
Password:
Password (again):
Superuser created successfully.
```

2. Aller sur l'URL suivant : `http://localhost:8000/admin/`

- Entrer les identifiants pour l'administrateur.
- Dans la partie administration je ne vois pas mes livres ni mes auteurs.

3. Aller dans le fichier **admin.py** de l'application **mangalib**.

4. Modifier les classes pour que dans la partie admin les métadonnées :

```python
class Meta:
  verbose_name = "Auteur"
  verbose_name_plural = "Auteurs"
```

- idem pour la classe **Book**.

5. Modifier les classes pour avoir les noms des articles de manière explicite :

```python
def __str__(self):
  return self.title
```

6. Modifier le nom d'une table à l'affichage :

```python
name = models.CharField(max_length=64, unique = True, verbose_name="Nom")
```

- Rajouter `verbose_name="Nom"` **!**

### Pour modifier l'interface administrateur :

1. Récupérer sur le code source de Django, les dossiers suivants : **Admin** et **registration**.
2. voici l'url : https://github.com/django/django/tree/main/django/contrib/admin/templates
3. Dans le la racine de notre projet (en dehors de toute application) : **créer un dossier `templates`** puis un dossier **admin**.
4. Mettre dans ce dossier les fichiers suivants trouvables dans le dossier **admin** :

- `base_site.html`
- `index.html`

5. Moddifier le fichier settings avec les modifications suivantes :

```python
'DIRS': [os.path.join(BASE_DIR, 'main/templates'),
        BASE_DIR / 'templates'],
```

---

## Les formulaires

1. Dans l'application **mangalib**, créer un fichier nommé **forms.py**.

- Il sert à regrouper tous les formulaires d'une même application.

2. Dans ce fichier j'écris cela :

```python
from django import forms

class SomeForm(forms.Form):
    username = forms.CharField(max_length=40)
```

- J'ai créé une classe **SomeForm** dans lequel j'ai créé un champ **username**.

3. Je vais maintenant dans le fichier **views.py** et je vais faire appel à mon formulaire pour le renvoyer sur la page.

- J'importe mon formulaire : `from .forms import SomeForm`
- Je modifie le la méthode index pour afficher mon formulaire :

```python
def index (request):
    if request.method == "POST":
        form = SomeForm(request.POST)

        if form.is_valid():
            return redirect('mangalib:index')
    else:
        form = SomeForm()

        context = {
        "books": Book.objects.all(),
        "form": form
        }
    return render(request, 'mangalib/index.html', context)
```

4. Dans mon template nommé **index.html** j'affiche mon formulaire :

```html
<h1>J'affiche mon formulaire</h1>
<form action="post">{% csrf_token %} {{ form }}</form>
```

5. Pour un champs où je rentre un mot de passe, j'écris la chose suivante :

```python
password = forms.CharField(label= "Mot de passe", widget=forms.PasswordInput)
```

- L'utilisation de `widget=forms.PasswordInput` garantit que le champ de mot de passe dans le formulaire est rendu de manière sécurisée, masquant les caractères saisis par l'utilisateur pour protéger la confidentialité du mot de passe.

6. Comment faire un formulaire de choix multiple :

```python
    langages = [('en', 'en'), ('fr', 'fr'), ('es', 'es'), ('pt-BR', 'pt-BR'),]
    # champs de formulaire
    langage = forms.MultipleChoiceField(label = "Langues", widget=forms.CheckboxSelectMultiple, choices=langages)
```

7. Les bouttons radio :

```python
from django import forms

class SomeForm(forms.Form):
    colors = [('1', 'rouge'), ('2', 'bleu'), ('3', 'blanc'), ('4', 'vert')]
    color = forms.ChoiceField(choices=colors, label="Couleurs", widget=forms.RadioSelect)
```

8. Les menus déroulans :

```python
from django import forms

class SomeForm(forms.Form):
    countries = [('1', 'France'), ('2', 'Suisse'), ('3', 'Espagne'), ('4', 'Italie')]
    country = forms.ChoiceField(choices=countries, label="Pays")
```

### Validation d'un champ spécifique :

1. Aller dans **forms.py** :

```python
    def clean_quantity(self):
        quantity = self.cleaned_data["quantity"]

        if quantity <= 0 or quantity > 100:
            raise forms.ValidationError("La quantité doit être compris entre 1 et 100")

        return quantity
```

2. Pour demander une double validation de mot de passe :

```python
# Dans forms.py
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")
```
