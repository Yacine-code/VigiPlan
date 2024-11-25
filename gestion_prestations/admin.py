from django.contrib import admin  # Importation de l'outil d'administration de Django
from .models import Prestation  # Importation du modèle Prestation

# Configuration de l'interface d'administration pour le modèle Prestation
@admin.register(Prestation)
class PrestationAdmin(admin.ModelAdmin):
    list_display = ['nom', 'site', 'date_debut', 'date_fin']  # Colonnes affichées dans la liste des prestations
    search_fields = ['nom', 'site__nom']  # Champs utilisables pour la recherche
    list_filter = ['site']  # Filtres par site disponibles dans l'interface
