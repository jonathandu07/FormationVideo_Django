from django.db import models

"""
class ModelA(Models.models):
    field = models.ManyToManyField(model) 
"""
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=64, unique = True, verbose_name="Nom")
    
    # Avoir un nom explicite dans l'administration
    def __str__(self):
        return self.name
    # pour la traduction modifier les métadonnées
    class Meta:
        verbose_name = "Auteur"
        verbose_name_plural = "Auteurs"
    
class Book(models.Model):
    title = models.CharField(max_length=32, unique = True, verbose_name="Titre")
    quantity = models.IntegerField(default=1, verbose_name="Quantité")
    # Première relation 
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, verbose_name="Auteur")
    
    # Avoir un nom explicite dans l'administration
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Livre"
        verbose_name_plural = "Livres"
        permissions = [
            ('apply_promo_code', 'Peut appliquer des réductions'),
        ]
    