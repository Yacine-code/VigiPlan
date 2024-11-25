from django.urls import path
from .views import AgentListView, AgentCreateView, AgentUpdateView, AgentDeleteView  
# Importation des vues pour la gestion des agents

# Définition des routes URL
urlpatterns = [
    path('', AgentListView.as_view(), name='agent-list'),  # Route pour la liste des agents
    path('create/', AgentCreateView.as_view(), name='agent-create'),  # Route pour créer un nouvel agent
    path('<int:pk>/update/', AgentUpdateView.as_view(), name='agent-update'),  # Route pour modifier un agent
    path('<int:pk>/delete/', AgentDeleteView.as_view(), name='agent-delete'),  # Route pour supprimer un agent
]
