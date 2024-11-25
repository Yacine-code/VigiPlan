from django.contrib import admin
from .models import Agent  # Importation du modèle Agent

# Configuration de l'interface d'administration pour le modèle Agent
@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenom', 'email', 'telephone', 'societe']  # Colonnes affichées dans la liste des agents
    search_fields = ['nom', 'prenom', 'email']  # Champs de recherche
    list_filter = ['societe']  # Filtres disponibles pour les sociétés
