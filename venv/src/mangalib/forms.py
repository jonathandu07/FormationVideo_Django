from django import forms

class SomeForm(forms.Form):
    username = forms.CharField(max_length=25, label="Nom d'utilisateur", required=False, )