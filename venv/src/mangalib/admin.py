from django.contrib import admin
from .models import Author, Book
# Register your models here.

# Ajout des models
admin.site.register(Author)
admin.site.register(Book)