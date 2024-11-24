from django import forms
from .models import Agent

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['nom', 'prenom', 'email', 'telephone', 'date_naissance', 'societe']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Agent.objects.filter(email=email).exists():
            raise forms.ValidationError("Cet email est déjà utilisé par un autre agent.")
        return email

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        if telephone and not telephone.isdigit():
            raise forms.ValidationError("Le numéro de téléphone doit contenir uniquement des chiffres.")
        return telephone
