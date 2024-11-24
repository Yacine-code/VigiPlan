from django import forms
from datetime import datetime, date, timedelta
from .models import Vacation

class VacationForm(forms.ModelForm):
    class Meta:
        model = Vacation
        fields = ['date', 'heure_debut', 'heure_fin', 'agent', 'prestation']

    def clean(self):
        cleaned_data = super().clean()
        heure_debut = cleaned_data.get('heure_debut')
        heure_fin = cleaned_data.get('heure_fin')

        # Vérification 1 : L'heure de début doit être antérieure à l'heure de fin
        if heure_debut and heure_fin:
            if heure_debut >= heure_fin:
                raise forms.ValidationError("L'heure de début doit être antérieure à l'heure de fin.")

            # Vérification 2 : La durée de la vacation ne doit pas dépasser 12 heures
            duration = datetime.combine(date.min, heure_fin) - datetime.combine(date.min, heure_debut)
            if duration > timedelta(hours=12):
                raise forms.ValidationError("Une vacation ne peut pas dépasser 12 heures.")

        return cleaned_data
