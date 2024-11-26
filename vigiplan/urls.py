from django.contrib import admin  # Importation de l'administration Django
from django.urls import path, include  # Pour définir les routes et inclure les URLs d'autres applications
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Bienvenue sur VigiPlan !</h1>")

# Définir les routes principales
urlpatterns = [
    path('admin/', admin.site.urls),  # Route pour l'administration
    path('agents/', include('gestion_agents.urls')),  # Routes pour les agents
    path('sites/', include('gestion_sites.urls')),  # Routes pour les sites
    path('prestations/', include('gestion_prestations.urls')),  # Routes pour les prestations
    path('vacations/', include('gestion_vacations.urls')),  # Routes pour les vacations
    path('', home_view),  # Route pour la page d'accueil
    path('', include('tableau_de_bord.urls')),  # Route racine pour le tableau de bord
]

