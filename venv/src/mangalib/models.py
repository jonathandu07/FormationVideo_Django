from django.db import models

"""
class ModelA(Models.models):
    field = models.ManyToManyField(model) 
"""
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=64, unique = True)
    
    
class Book(models.Model):
    title = models.CharField(max_length=32, unique = True)
    quantity = models.IntegerField(default=1)
    # Première relation 
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    
    
    