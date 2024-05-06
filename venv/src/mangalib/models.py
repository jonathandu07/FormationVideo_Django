from django.db import models

"""
class ModelA(Models.models):
    field = models.ManyToManyField(model) 
"""
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=64, unique = True)
    
    # pour la traduction modifier les métadonnées
    class Meta:
        verbose_name = "Auteur"
        verbose_name_plural = "Auteurs"
    
class Book(models.Model):
    title = models.CharField(max_length=32, unique = True)
    quantity = models.IntegerField(default=1)
    # Première relation 
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    
    class Meta:
        verbose_name = "Livre"
        verbose_name_plural = "Livres"
    