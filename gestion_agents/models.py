from django.db import models
from gestion_societes.models import Société

class Agent(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    date_naissance = models.DateField(blank=True, null=True)
    societe = models.ForeignKey(Société, on_delete=models.CASCADE, related_name="agents")

    def __str__(self):
        return f"{self.prenom} {self.nom}"
