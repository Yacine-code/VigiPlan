from django.urls import path  # Importation pour définir les routes URL
from .views import SiteListView, SiteCreateView, SiteUpdateView, SiteDeleteView  
# Importation des vues associées aux sites

# Routes pour la gestion des sites
urlpatterns = [
    path('', SiteListView.as_view(), name='site-list'),  # Route pour afficher la liste des sites
    path('create/', SiteCreateView.as_view(), name='site-create'),  # Route pour créer un nouveau site
    path('<int:pk>/update/', SiteUpdateView.as_view(), name='site-update'),  # Route pour modifier un site existant
    path('<int:pk>/delete/', SiteDeleteView.as_view(), name='site-delete'),  # Route pour supprimer un site
]
