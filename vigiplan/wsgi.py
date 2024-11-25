"""
WSGI configuration pour le projet vigiplan.
Utilisé pour déployer le projet avec un serveur compatible WSGI.
"""

import os  # Gestion des variables d'environnement
from django.core.wsgi import get_wsgi_application  # Fonction pour obtenir l'application WSGI

# Définir les paramètres du projet pour le serveur
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vigiplan.settings')

# Créer l'application WSGI
application = get_wsgi_application()
