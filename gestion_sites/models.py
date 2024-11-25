from django.db import models  # Importation de l'outil pour définir les modèles
from gestion_societes.models import Société  # Importation du modèle Société pour établir une relation

# Modèle représentant un site associé à une société
class Site(models.Model):
    nom = models.CharField(max_length=100)  # Champ pour le nom du site (max 100 caractères)
    adresse = models.TextField(blank=True, null=True)  # Champ optionnel pour l'adresse complète du site
    ville = models.CharField(max_length=50, blank=True, null=True)  # Champ optionnel pour la ville
    societe = models.ForeignKey(Société, on_delete=models.CASCADE, related_name="sites")  
    # Relation entre un site et une société. Si la société est supprimée, les sites associés le seront aussi.

    def __str__(self):
        return f"{self.nom} - {self.ville}"  # Représentation lisible du site
