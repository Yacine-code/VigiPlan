from django.db import models  # Importation de l'outil de gestion des modèles Django
from gestion_sites.models import Site  # Importation du modèle Site pour la relation
from django.core.exceptions import ValidationError  # Importation pour lever des erreurs de validation personnalisées

# Modèle représentant une prestation associée à un site
class Prestation(models.Model):
    nom = models.CharField(max_length=100)  # Champ pour le nom de la prestation, avec une limite de 100 caractères
    description = models.TextField(blank=True, null=True)  # Champ optionnel pour une description détaillée
    date_debut = models.DateField()  # Champ obligatoire pour la date de début de la prestation
    date_fin = models.DateField(blank=True, null=True)  # Champ optionnel pour la date de fin
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name="prestations")  
    # Relation avec un site, suppression des prestations si le site est supprimé

    def __str__(self):
        return f"{self.nom} ({self.site.nom})"  # Retourne une représentation lisible de l'objet

    def clean(self):
        # Méthode pour valider les données avant l'enregistrement
        if self.date_debut and self.date_fin and self.date_debut > self.date_fin:
            raise ValidationError("La date de début doit être antérieure ou égale à la date de fin.")  
            # Vérifie que la date de début est avant la date de fin
