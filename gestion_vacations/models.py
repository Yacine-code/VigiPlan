from django.db import models
from django.core.exceptions import ValidationError
from gestion_prestations.models import Prestation
from gestion_agents.models import Agent
from datetime import datetime, date, timedelta


class Vacation(models.Model):
    date = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    agent = models.ForeignKey(
        Agent, on_delete=models.SET_NULL, null=True, blank=True, related_name="vacations"
    )
    prestation = models.ForeignKey(
        Prestation, on_delete=models.CASCADE, related_name="vacations"
    )

    def __str__(self):
        return f"{self.date} ({self.heure_debut} - {self.heure_fin}) - {self.agent or 'Non affectée'}"

    def clean(self):
        # Validation pour vérifier les heures
        if self.heure_debut >= self.heure_fin:
            raise ValidationError("L'heure de début doit être antérieure à l'heure de fin.")

 # Validation pour vérifier la durée maximale de la vacation (12 heures)
        duration = datetime.combine(date.min, self.heure_fin) - datetime.combine(date.min, self.heure_debut)
        if duration > timedelta(hours=12):
            raise ValidationError("Une vacation ne peut pas dépasser 12 heures.")