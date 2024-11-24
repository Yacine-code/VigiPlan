from django.db import models
from gestion_societes.models import Société

class Site(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField(blank=True, null=True)
    ville = models.CharField(max_length=50, blank=True, null=True)
    societe = models.ForeignKey(Société, on_delete=models.CASCADE, related_name="sites")

    def __str__(self):
        return f"{self.nom} - {self.ville}"
