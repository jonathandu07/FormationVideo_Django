from django import forms
from .models import Author, Book

class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all(),label="Auteur")
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'quantity']
        lables = {'titles': 'Titre', 'quantity': 'Quantité'}
        
    
    # Méthode pour vérifier le champs quantité
    def clean_quantity(self):
        quantity = self.cleaned_data["quantity"]
        
        if quantity <= 0 or quantity > 100:
            raise forms.ValidationError("La quantité doit être compris entre 1 et 100")
        
        return quantity