from django.apps import AppConfig  # Importation pour configurer l'application

# Configuration de l'application gestion_sites
class GestionSitesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Type de clé primaire par défaut
    name = 'gestion_sites'  # Nom de l'application
