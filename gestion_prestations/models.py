from django.db import models
from gestion_sites.models import Site
from django.core.exceptions import ValidationError
class Prestation(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_debut = models.DateField()
    date_fin = models.DateField(blank=True, null=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name="prestations")

    def __str__(self):
        return f"{self.nom} ({self.site.nom})"


    def clean(self):
        # Valide les dates directement dans le modèle
        if self.date_debut and self.date_fin and self.date_debut > self.date_fin:
            raise ValidationError("La date de début doit être antérieure ou égale à la date de fin.")