from django import forms  # Importation des outils pour créer des formulaires
from datetime import datetime, date, timedelta  # Pour manipuler les heures et les durées
from .models import Vacation  # Importation du modèle Vacation

# Formulaire personnalisé pour le modèle Vacation
class VacationForm(forms.ModelForm):
    class Meta:
        model = Vacation  # Modèle associé au formulaire
        fields = ['date', 'heure_debut', 'heure_fin', 'agent', 'prestation']  
        # Champs inclus dans le formulaire

    def clean(self):
        # Validation des données du formulaire
        cleaned_data = super().clean()
        heure_debut = cleaned_data.get('heure_debut')
        heure_fin = cleaned_data.get('heure_fin')

        if heure_debut and heure_fin:
            if heure_debut >= heure_fin:
                raise forms.ValidationError("L'heure de début doit être antérieure à l'heure de fin.")

            duration = datetime.combine(date.min, heure_fin) - datetime.combine(date.min, heure_debut)
            if duration > timedelta(hours=12):
                raise forms.ValidationError("Une vacation ne peut pas dépasser 12 heures.")

        return cleaned_data
