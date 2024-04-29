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

10. bis **pour retirer l'érreur suivante :**
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
