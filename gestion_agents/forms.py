from django import forms
from .models import Agent  # Importation du modèle Agent

# Formulaire personnalisé pour le modèle Agent
class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent  # Modèle associé
        fields = ['nom', 'prenom', 'email', 'telephone', 'date_naissance', 'societe']  
        # Champs inclus dans le formulaire

    # Validation personnalisée pour l'email
    def clean_email(self):
        email = self.cleaned_data.get('email')  # Récupération de l'email
        if Agent.objects.filter(email=email).exists():  # Vérification si l'email existe déjà
            raise forms.ValidationError("Cet email est déjà utilisé par un autre agent.")  # Erreur si doublon
        return email

    # Validation personnalisée pour le numéro de téléphone
    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')  # Récupération du téléphone
        if telephone and not telephone.isdigit():  # Vérification si contient uniquement des chiffres
            raise forms.ValidationError("Le numéro de téléphone doit contenir uniquement des chiffres.")  # Erreur sinon
        return telephone
