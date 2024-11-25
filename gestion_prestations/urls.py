from django.urls import path  # Importation pour définir les routes URL
from .views import PrestationListView, PrestationCreateView, PrestationUpdateView, PrestationDeleteView  
# Importation des vues associées aux prestations

# Liste des routes pour les fonctionnalités CRUD sur les prestations
urlpatterns = [
    path('', PrestationListView.as_view(), name='prestation-list'),  # Route pour afficher la liste des prestations
    path('create/', PrestationCreateView.as_view(), name='prestation-create'),  # Route pour créer une prestation
    path('<int:pk>/update/', PrestationUpdateView.as_view(), name='prestation-update'),  # Route pour modifier une prestation
    path('<int:pk>/delete/', PrestationDeleteView.as_view(), name='prestation-delete'),  # Route pour supprimer une prestation
]
