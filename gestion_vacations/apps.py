from django.apps import AppConfig  # Pour configurer l'application Django

# Configuration de l'application gestion_vacations
class GestionVacationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Type de clé primaire par défaut
    name = 'gestion_vacations'  # Nom de l'application
