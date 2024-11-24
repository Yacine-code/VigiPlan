from django import forms
from .models import Prestation

class PrestationForm(forms.ModelForm):
    class Meta:
        model = Prestation
        fields = ['nom', 'description', 'date_debut', 'date_fin', 'site']
