from django.urls import path
from . import views

# Je crréais une variable pour mon app
app_name = "mangalib"
urlpatterns = [
    path('', views.index, name='index'), # manga/
    # Show est la méthode qui est dans views.py
    path("<int:book_id>/", views.show, name="show"), # manga/<id>
    path('ajouter-livre/', views.add, name="add"),
    path('modifier-livre/<int:book_id>/', views.edit, name="edit"),
    path('supprimer-livre/<int:book_id>/', views.remove, name="delete"),
]