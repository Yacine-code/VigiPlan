from pathlib import Path  # Importation pour la gestion des chemins

# Définir le chemin de base du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuration de la base de données PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Utilisation de PostgreSQL comme backend
        'NAME': 'vigiplan_db',  # Nom de la base de données
        'USER': 'vigiplan_user',  # Nom d'utilisateur
        'PASSWORD': 'mot_de_passe_secure',  # Mot de passe sécurisé
        'HOST': 'localhost',  # Adresse du serveur de base de données
        'PORT': '5432',  # Port utilisé par PostgreSQL
    }
}

# Clé secrète pour les fonctionnalités sécurisées de Django
SECRET_KEY = 'django-insecure-s-r7iajxqvp64uwp3sk*bpcz!#35p_sbjd2!!tm$whfumoo^)s'

# Activer ou désactiver le mode de débogage
DEBUG = True  # À mettre sur False en production

# Hôtes autorisés à accéder au projet
ALLOWED_HOSTS = []

# Définir le modèle utilisateur personnalisé
AUTH_USER_MODEL = 'gestion_utilisateurs.CustomUser'

# Applications installées dans le projet
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gestion_utilisateurs',  # Module de gestion des utilisateurs
    'gestion_societes',  # Module de gestion des sociétés
    'gestion_agents',  # Module de gestion des agents
    'gestion_sites',  # Module de gestion des sites
    'gestion_prestations',  # Module de gestion des prestations
    'gestion_vacations',  # Module de gestion des vacations
]

# Paramètres linguistiques et temporels
LANGUAGE_CODE = 'fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Middleware activés
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Sécurité de la communication
    'django.contrib.sessions.middleware.SessionMiddleware',  # Gestion des sessions
    'django.middleware.common.CommonMiddleware',  # Middleware pour les requêtes générales
    'django.middleware.csrf.CsrfViewMiddleware',  # Protection CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Authentification utilisateur
    'django.contrib.messages.middleware.MessageMiddleware',  # Gestion des messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Protection contre le clickjacking
]

# Configuration des URL principales
ROOT_URLCONF = 'vigiplan.urls'

# Configuration des templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Backend des templates
        'DIRS': [],  # Dossiers personnalisés pour les templates
        'APP_DIRS': True,  # Recherche des templates dans les applications
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuration WSGI
WSGI_APPLICATION = 'vigiplan.wsgi.application'

# Validation des mots de passe
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# URL des fichiers statiques
STATIC_URL = 'static/'

# Type de clé primaire par défaut
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
