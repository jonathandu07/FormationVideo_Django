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
