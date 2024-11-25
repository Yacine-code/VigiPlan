from django.contrib import admin  # Importation de l'outil d'administration Django
from .models import Site  # Importation du modèle Site

# Configuration de l'interface d'administration pour le modèle Site
@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['nom', 'ville', 'societe']  # Colonnes affichées dans la liste des sites
    search_fields = ['nom', 'ville']  # Champs utilisables pour la recherche
    list_filter = ['ville', 'societe']  # Filtres disponibles pour trier les sites
