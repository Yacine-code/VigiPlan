from django.db import models
from gestion_societes.models import Société  # Importation du modèle Société depuis l'application gestion_societes

# Modèle Agent, représente un agent lié à une société
class Agent(models.Model):
    nom = models.CharField(max_length=100)  # Champ pour le nom de l'agent (max 100 caractères)
    prenom = models.CharField(max_length=100)  # Champ pour le prénom de l'agent (max 100 caractères)
    email = models.EmailField(unique=True)  # Champ pour l'email, doit être unique
    telephone = models.CharField(max_length=15, blank=True, null=True)  # Champ optionnel pour le téléphone
    date_naissance = models.DateField(blank=True, null=True)  # Champ optionnel pour la date de naissance
    societe = models.ForeignKey(Société, on_delete=models.CASCADE, related_name="agents")  
    # Relation entre l'agent et une société, suppression en cascade si la société est supprimée

    def __str__(self):
        return f"{self.prenom} {self.nom}"  # Affichage de l'agent sous forme 'Prénom Nom'
