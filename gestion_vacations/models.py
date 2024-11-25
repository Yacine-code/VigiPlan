from django.db import models  # Importation pour la définition des modèles
from django.core.exceptions import ValidationError  # Importation pour lever des erreurs de validation
from gestion_prestations.models import Prestation  # Importation du modèle Prestation pour la relation
from gestion_agents.models import Agent  # Importation du modèle Agent pour la relation
from datetime import datetime, date, timedelta  # Importation des outils pour la manipulation des dates et heures

# Modèle représentant une vacation associée à une prestation et éventuellement à un agent
class Vacation(models.Model):
    date = models.DateField()  # Champ pour la date de la vacation
    heure_debut = models.TimeField()  # Champ pour l'heure de début
    heure_fin = models.TimeField()  # Champ pour l'heure de fin
    agent = models.ForeignKey(
        Agent, on_delete=models.SET_NULL, null=True, blank=True, related_name="vacations"
    )  
    # Relation optionnelle avec un agent. Si l'agent est supprimé, le champ est mis à NULL.
    prestation = models.ForeignKey(
        Prestation, on_delete=models.CASCADE, related_name="vacations"
    )  
    # Relation obligatoire avec une prestation. La suppression de la prestation entraîne celle des vacations associées.

    def __str__(self):
        # Représentation lisible de la vacation
        return f"{self.date} ({self.heure_debut} - {self.heure_fin}) - {self.agent or 'Non affectée'}"

    def clean(self):
        # Validation des données avant l'enregistrement
        if self.heure_debut >= self.heure_fin:
            raise ValidationError("L'heure de début doit être antérieure à l'heure de fin.")

        duration = datetime.combine(date.min, self.heure_fin) - datetime.combine(date.min, self.heure_debut)
        if duration > timedelta(hours=12):
            raise ValidationError("Une vacation ne peut pas dépasser 12 heures.")
