from django import forms
from .models import Author, Book

class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all(),label="Auteur")
    
    class Meta:
        model = Book
        fields = ['tile', 'author', 'quantity']
        lables = {'titles': 'Titre', 'quantity': 'Quantité'}