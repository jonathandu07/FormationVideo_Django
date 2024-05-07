from django import forms

class SomeForm(forms.Form):
    # username = forms.CharField(max_length=25, label="Nom d'utilisateur", required=False, )
    # password = forms.CharField(label= "Mot de passe", widget=forms.PasswordInput)
    # #  Pour les zone de texte dans un formulaire
    # bio = forms.CharField(label= "Biographie", widget=forms.Textarea)
    # publicate = forms.BooleanField(label="Choix")
    # valider = forms.CharField(label = "Valider", widget=forms.CheckboxInput)
    # langages = [('en', 'en'), ('fr', 'fr'), ('es', 'es'), ('pt-BR', 'pt-BR'),]
    # # champs de formulaire
    # langage = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=langages)
    colors = [('1', 'rouge'), ('2', 'bleu'), ('3', 'blanc'), ('4', 'vert')]
    color = forms.ChoiceField(choices=colors, label="Couleurs", widget=forms.RadioSelect)