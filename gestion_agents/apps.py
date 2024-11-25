from django.apps import AppConfig

# Configuration de l'application gestion_agents
class GestionAgentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Type de clé primaire par défaut
    name = 'gestion_agents'  # Nom de l'application
