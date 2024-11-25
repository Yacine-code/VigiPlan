from django import forms  # Importation des outils de formulaires de Django
from .models import Prestation  # Importation du modèle Prestation

# Formulaire personnalisé pour le modèle Prestation
class PrestationForm(forms.ModelForm):
    class Meta:
        model = Prestation  # Modèle associé au formulaire
        fields = ['nom', 'description', 'date_debut', 'date_fin', 'site']  
        # Champs inclus dans le formulaire
